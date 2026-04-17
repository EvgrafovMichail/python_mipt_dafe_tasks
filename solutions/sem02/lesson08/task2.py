import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    rows, cols = maze.shape
    grid = maze.copy()
    grid[:] = -1
    grid[start] = 0
    current = 0
    found = False
    frames = []
    frames.append(grid.copy())

    while np.any(current == grid):
        front = current == grid

        if grid[end] != -1:
            found = True
            break

        neighbors = np.zeros(shape=front.shape, dtype=front.dtype)
        neighbors[1:, :] |= front[:-1, :]
        neighbors[:-1, :] |= front[1:, :]
        neighbors[:, 1:] |= front[:, :-1]
        neighbors[:, :-1] |= front[:, 1:]

        new_point = neighbors & (maze == 1) & (grid == -1)

        grid[new_point] = current + 1
        frames.append(grid.copy())

        current += 1

    if not found:
        print("Пути не существует")
        return 0

    fig, ax = plt.subplots(figsize=(rows, cols))

    def prepare_data(data):
        display = data.astype(float)
        display[maze == 0] = -10
        display[(maze == 1) & (data == -1)] = -5
        return display

    im = ax.imshow(prepare_data(frames[0]), cmap="viridis")

    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which="minor", color="#FFF200FF", linestyle="-", linewidth=0.5)

    text_objects = [
        [
            ax.text(j, i, "", ha="center", va="center", fontsize=12, fontweight="bold")
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    def update(frame_idx):
        data = frames[frame_idx]
        im.set_array(prepare_data(data))

        for i in range(rows):
            for j in range(cols):
                val = data[i, j]
                if val >= 0:
                    text_objects[i][j].set_text(str(val))
                    text_objects[i][j].set_color("black")
                else:
                    text_objects[i][j].set_text("")
        return [im]

    ani = FuncAnimation(fig, update, frames=len(frames), interval=150, blit=False)

    if save_path:
        ani.save(save_path, writer="pillow")

    # plt.show()
    return ani


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

    start = (2, 0)
    end = (5, 0)
    save_path = "solutions/sem02/lesson08/labyrinth.gif"  # Укажите путь для сохранения анимации

    animation = animate_wave_algorithm(maze, start, end, save_path)
    HTML(animation.to_jshtml())

    # Пример 2

    maze_path = "solutions/sem02/lesson08/data/maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (2, 0)
    end = (5, 0)
    loaded_save_path = "solutions/sem02/lesson08/loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
