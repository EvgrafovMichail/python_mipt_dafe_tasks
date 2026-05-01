import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def shift(array, direction):
    if direction == "up":
        shifted_arr = np.vstack((array.copy()[1:], np.full(array.shape[1], -1)))
    elif direction == "down":
        shifted_arr = np.vstack((np.full(array.shape[1], -1), array.copy()[:-1]))
    elif direction == "right":
        shifted_arr = np.hstack((np.full(array.shape[0], -1)[:, np.newaxis], array.copy()[:, :-1]))
    elif direction == "left":
        shifted_arr = np.hstack((array.copy()[:, 1:], np.full(array.shape[0], -1)[:, np.newaxis]))
    return shifted_arr


def update_route(maze: np.ndarray, distances: np.ndarray, step: int):
    mask_of_change = (
        (maze != 0)
        & (distances < 0)
        & (
            (shift(distances, "up") != -1)
            | (shift(distances, "down") != -1)
            | (shift(distances, "right") != -1)
            | (shift(distances, "left") != -1)
        )
    )
    if np.any(mask_of_change):
        distances[mask_of_change] = step
        return 0
    return -1


def reconstruct_path(distances, start, end):
    path = []
    current = end

    if distances[current] == -1:
        return path

    while current != start:
        y, x = current
        neighbors = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        found = False

        for ny, nx in neighbors:
            if (
                0 <= ny < distances.shape[0]
                and 0 <= nx < distances.shape[1]
                and distances[ny, nx] == distances[current] - 1
            ):
                current = (ny, nx)
                path.append(current)
                found = True
                break

        if not found:
            break

    return path


def create_updater(maze, distances, start, end, im, ax):
    step = 1
    path_found = False
    full_path = []
    path_step = 0
    max_distance = maze.shape[0] * maze.shape[1]

    texts = {}

    def update(frame):
        nonlocal step, path_found, full_path, path_step

        if not path_found:
            result = update_route(maze, distances, step)

            if result == -1:
                rgb = np.zeros((*maze.shape, 3))
                rgb[maze == 0] = [0, 0, 0]
                rgb[maze == 1] = [0.5, 0.5, 0.5]
                im.set_array(rgb)
                ax.text(
                    maze.shape[1] / 2,
                    maze.shape[0] / 2,
                    "ПУТЬ НЕ СУЩЕСТВУЕТ!!!",
                    ha="center",
                    va="center",
                    color="red",
                    fontsize=14,
                    fontweight="bold",
                )
                return [im]

            step += 1

            rgb = np.zeros((*maze.shape, 3))
            rgb[maze == 0] = [0, 0, 0]
            rgb[maze == 1] = [1, 1, 1]

            for s in range(step):
                t = s / max_distance
                rgb[distances == s] = [0.3, 0.5, 1 - t]

            for s in range(step):
                cells = np.argwhere(distances == s)
                for y, x in cells:
                    if maze[y, x] != 0 and (y, x) not in texts:
                        text = ax.text(
                            x,
                            y,
                            str(s),
                            ha="center",
                            va="center",
                            color="black",
                            fontsize=8,
                            fontweight="bold",
                        )
                        texts[(y, x)] = text

            if distances[end] != -1 and not path_found:
                path_found = True
                full_path = reconstruct_path(distances, start, end)
                path_step = 0

        else:
            rgb = np.zeros((*maze.shape, 3))
            rgb[maze == 0] = [0, 0, 0]
            rgb[maze == 1] = [0.6, 0.6, 0.6]

            for s in range(1, step):
                rgb[distances == s] = [0.7, 0.8, 1]

            for i in range(path_step):
                y, x = full_path[i]
                if maze[y, x] != 0:
                    rgb[y, x] = [0, 1, 0]

            rgb[start] = [1, 0, 0]
            if maze[end] != 0:
                rgb[end] = [0, 0, 1]

            if (end[0], end[1]) in texts:
                texts[(end[0], end[1])].set_color("white")

            if path_step < len(full_path):
                path_step += 1

        im.set_array(rgb)
        return [im] + list(texts.values())

    return update


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    distances = np.full_like(maze, -1, dtype=np.int32)
    distances[start] = 0

    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(np.zeros((*maze.shape, 3)), aspect="equal")

    ax.set_title("Волновой алгоритм")
    ax.set_xticks(np.arange(maze.shape[1]))
    ax.set_yticks(np.arange(maze.shape[0]))
    ax.grid(which="major", visible=False)

    ax.set_xticks(np.arange(-0.5, maze.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, maze.shape[0], 1), minor=True)
    ax.grid(which="minor", color="black", linestyle="-", linewidth=1.5)

    ax.tick_params(which="minor", size=0)

    updater = create_updater(maze, distances, start, end, im, ax)

    anim = FuncAnimation(
        fig, updater, frames=None, interval=200, repeat=False, cache_frame_data=False
    )

    if save_path:
        anim.save(save_path, writer="pillow", fps=5)

    return anim


if __name__ == "__main__":
    # Пример 1
    maze = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    )

    start = (3, 3)
    end = (96, 3)
    save_path = "labyrinth.gif"  # Укажите путь для сохранения анимации

    # animation = animate_wave_algorithm(maze, start, end, "")
    #   HTML(animation.to_jshtml())

    # Пример 2

    maze_path = ""
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (3, 3)
    end = (54, 4)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, "")
    plt.show()
#  HTML(loaded_animation.to_jshtml())
