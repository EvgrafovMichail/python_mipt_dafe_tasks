from functools import partial

import matplotlib as mpl
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from matplotlib.cm import ScalarMappable
from matplotlib.colors import LinearSegmentedColormap, Normalize


def calculate_wave_propagation(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int]
) -> tuple[list[np.ndarray], list[tuple[int, int]]]:
    rows, cols = maze.shape
    distances = np.full((rows, cols), -1, dtype=int)
    distances[start] = 0

    queue = [start]
    history = [distances.copy()]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    found = False

    while queue and not found:
        next_queue = []
        for r, c in queue:
            if (r, c) == end:
                found = True
                break

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if maze[nr, nc] == 1 and distances[nr, nc] == -1:
                        distances[nr, nc] = distances[r, c] + 1
                        next_queue.append((nr, nc))

        if not found:
            queue = next_queue
            if queue:
                history.append(distances.copy())
        else:
            history.append(distances.copy())

    path = []
    if found:
        curr = end
        path.append(curr)
        while curr != start:
            r, c = curr
            curr_dist = distances[r, c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if distances[nr, nc] == curr_dist - 1:
                        curr = (nr, nc)
                        path.append(curr)
                        break
        path.reverse()

    return history, path


def update_frame(
    frame_id: int,
    *,
    ax_img: mpimg.AxesImage,
    history: list[np.ndarray],
    path: list[tuple[int, int]],
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[mpimg.AxesImage]:
    max_dist = np.max(history[-1]) if history else 1
    history_len = len(history)
    path_len = len(path) if path else 0

    if frame_id < history_len:
        distances = history[frame_id]
        current_path = []
    elif frame_id < history_len + path_len:
        distances = history[-1]
        step = frame_id - history_len + 1
        current_path = path[-step:]
    else:
        distances = history[-1]
        current_path = path

    rows, cols = maze.shape
    img = np.zeros((rows, cols, 3))

    img[maze == 0] = [0.2, 0.2, 0.2]
    img[maze == 1] = [1.0, 1.0, 1.0]

    mask = distances >= 0
    if np.any(mask):
        norm_dist = distances[mask] / max(max_dist, 1)
        img[mask, 0] = 0.2
        img[mask, 1] = 1.0 - 0.6 * norm_dist
        img[mask, 2] = 1.0

    if current_path:
        path_x, path_y = zip(*current_path)
        img[path_x, path_y] = [1.0, 0.8, 0.0]

    img[start] = [0.0, 0.8, 0.0]
    img[end] = [0.8, 0.0, 0.0]

    ax_img.set_data(img)
    return (ax_img,)


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    history, path = calculate_wave_propagation(maze, start, end)

    if not path:
        print(f"Путь от {start} к {end} не существует!")

    fig, ax = plt.subplots(figsize=(6, 6))

    colors = [(0.2, 1.0, 1.0), (0.2, 0.4, 1.0)]
    custom_cmap = LinearSegmentedColormap.from_list("cmap", colors)

    norm = Normalize(vmin=0, vmax=np.max(history[-1]))
    sm = ScalarMappable(norm=norm, cmap=custom_cmap)
    fig.colorbar(sm, ax=ax)

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_xticks(np.arange(-0.5, maze.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, maze.shape[0], 1), minor=True)
    ax.grid(which="minor", color="black", linestyle="-", linewidth=1)
    ax.tick_params(which="minor", size=0)

    img = np.zeros((maze.shape[0], maze.shape[1], 3))
    ax_img = ax.imshow(img, interpolation="nearest")

    total_frames = len(history) + (len(path) if path else 0) + 10

    anim_func = partial(
        update_frame, ax_img=ax_img, history=history, path=path, maze=maze, start=start, end=end
    )

    anim = FuncAnimation(fig, anim_func, frames=total_frames, interval=100, blit=True)

    if save_path:
        anim.save(save_path, writer="pillow", fps=10)

    return anim


if __name__ == "__main__":
    mpl.rcParams["animation.embed_limit"] = 100.0
    # Пример 1
    maze_1 = np.array(
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

    start_1 = (2, 0)
    end_1 = (5, 0)
    save_path_1 = "labyrinth.gif"

    animation = animate_wave_algorithm(maze_1, start_1, end_1, save_path_1)
    HTML(animation.to_jshtml())

    # Пример 2
    maze_path = "./data/maze.npy"

    loaded_maze = np.load(maze_path)
    start_2 = (0, 18)
    end_2 = (101, 43)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start_2, end_2, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
