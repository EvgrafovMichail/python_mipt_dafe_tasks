from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation

class Wrong_Using_Error(Exception):
    pass

def mark_cells(visited_cells, start_x, start_y):
    if (
        start_x < 0
        or start_x >= visited_cells.shape[0]
        or start_y < 0
        or start_y >= visited_cells.shape[1]
    ):
        raise Wrong_Using_Error("Начальная точка находится за пределами лабиринта")

    if visited_cells[start_x, start_y] != -1:
        raise Wrong_Using_Error("Начальная точка находится в стене")


    step = 0
    squares = [(start_x, start_y, step)]
    current = 0

    while current < len(squares):
        x, y, step = squares[current]
        current += 1

        if x < 0 or x >= visited_cells.shape[0] or y < 0 or y >= visited_cells.shape[1]:
            continue

        if visited_cells[x, y] != -1:
            continue

        visited_cells[x, y] = step

        squares.append((x + 1, y, step + 1))
        squares.append((x - 1, y, step + 1))
        squares.append((x, y + 1, step + 1))
        squares.append((x, y - 1, step + 1))


def is_there_way_out(visited_cells, end):
    if visited_cells[end] == -1:
        print("Пути до выхода не существует")


def image_maze(axis, maze):
    x_size, y_size = maze.shape[1], maze.shape[0]
    axis.set_title("Wellenalgorithmus\n(Wave algorithm)", fontsize=17, fontweight="bold")

    axis.set_xticks(np.arange(0, x_size, max(1, x_size // 10)))
    axis.set_yticks(np.arange(0, y_size, max(1, y_size // 10)))

    axis.set_xticks(np.arange(-0.5, x_size, 1), minor=True)
    axis.set_yticks(np.arange(-0.5, y_size, 1), minor=True)

    axis.tick_params(axis="both", which="major", labelsize=12, width=3)

    axis.grid(True, which="minor", linewidth=2, color="black", alpha=1)
    axis.grid(False, which="major")

    axis.set_xlim(-0.5, x_size - 0.5)
    axis.set_ylim(y_size - 0.5, -0.5)

    way = np.zeros((maze.shape[0], maze.shape[1], 4))
    way[maze == 0] = [0.55, 0.27, 0.07, 1]
    way[maze != 0] = [1, 1, 1, 1]

    axis.imshow(way, extent=[-0.5, x_size - 0.5, y_size - 0.5, -0.5], origin="upper", alpha=1)


def animate_wave_algorithm(maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    visited_cells = -1 * maze.astype(np.int32)

    mark_cells(visited_cells, *start)
    is_there_way_out(visited_cells, end)

    figure, axis = plt.subplots(figsize=(10, 10))

    colored = np.zeros((*maze.shape, 4))
    colored[start] = [1, 0.84, 0, 1]

    overlay = axis.imshow(colored,
                          extent=[-0.5, maze.shape[1]-0.5, maze.shape[0]-0.5, -0.5],
                          origin="upper", alpha=0.8, zorder=2)

    image_maze(axis, maze)

    distance_max = np.max(visited_cells)
    
    wave_frames = []
    for dist in range(distance_max + 1):
        rows, cols = np.where(visited_cells == dist)
        wave_frames.append((rows, cols))

    def update(frame):
        if frame <= distance_max:
            rows, cols = wave_frames[frame]
            for i in range(len(rows)):
                r = rows[i]
                c = cols[i]
                if visited_cells[r, c] > 0:
                    colored[r, c] = [1, 0.84, 0, 1]

        overlay.set_data(colored)
        return overlay,

    animation = FuncAnimation(figure, update, frames=distance_max + 1, interval=100)

    if save_path:
        animation.save(save_path, writer="pillow", fps=5)

    return animation


if __name__ == "__main__":
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
    save_path = "labyrinth.gif"

    animation = animate_wave_algorithm(maze, start, end, save_path)
    HTML(animation.to_jshtml())

    maze_path = "solutions/sem02/lesson08/data/maze.npy"
    loaded_maze = np.load(maze_path)

    start = (30, 4)
    end = (100, 43)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())