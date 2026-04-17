import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from typing import Tuple, Optional


def is_cell_not_in_walk_place(visited_cells: np.ndarray, x: int, y: int) -> bool:
    return not (0 <= x < visited_cells.shape[0] and 0 <= y < visited_cells.shape[1]) or visited_cells[x, y] != -1

def mark_cells(visited_cells: np.ndarray, start_x: int, start_y: int) -> None:
    if is_cell_not_in_walk_place(visited_cells, start_x, start_y):
        print("Начальная точка находится за пределами дорожки, по которой можно ходить")
        return

    step = 0
    cells = [(start_x, start_y, step)]
    curr = 0

    while curr < len(cells):
        curr_x, curr_y, step = cells[curr]
        curr += 1

        if is_cell_not_in_walk_place(visited_cells, curr_x, curr_y):
            continue

        visited_cells[curr_x, curr_y] = step

        cells.append((curr_x + 1, curr_y, step + 1))
        cells.append((curr_x - 1, curr_y, step + 1))
        cells.append((curr_x, curr_y + 1, step + 1))
        cells.append((curr_x, curr_y - 1, step + 1))


def image_maze(axis: plt.Axes, maze: np.ndarray) -> None:
    x_size, y_size = maze.shape[1], maze.shape[0]
    axis.set_title("Волновой алгоритм", fontsize=17, fontweight="bold")

    axis.set_xticks(np.arange(0, x_size, max(1, x_size // 10)))
    axis.set_yticks(np.arange(0, y_size, max(1, y_size // 10)))

    axis.set_xticks(np.arange(-0.5, x_size, 1), minor=True)
    axis.set_yticks(np.arange(-0.5, y_size, 1), minor=True)

    axis.tick_params(axis="both", which="major", labelsize=12, width=3)

    axis.grid(True, which="minor", linewidth=2, color="black")
    axis.grid(False, which="major")

    axis.set_xlim(-0.5, x_size - 0.5)
    axis.set_ylim(y_size - 0.5, -0.5)

    way_mask = maze != 0
    way = np.zeros((maze.shape[0], maze.shape[1], 4))
    way[way_mask] = [0, 0, 0, 1]            # черный цвет

    image_edge = [-0.5, x_size - 0.5, y_size - 0.5, -0.5]
    axis.imshow(way, extent=image_edge, origin="upper")


def animate_wave_algorithm(
    maze: np.ndarray, start: Tuple[int, int], end: Tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    visited_cells = -1 * maze.astype(np.int32)

    mark_cells(visited_cells, *start)
    
    if visited_cells[end] == -1:
        print("Пути до выхода не существует")

    figure, axis = plt.subplots(figsize=(10, 10))

    marker_size = 350 / max(*maze.shape)
    x_points = np.array([])
    y_points = np.array([])
    wave, *_ = axis.plot(x_points, y_points, "o", ms=marker_size)
    end_point, *_ = axis.plot([], [], "o", ms=marker_size, c="orange")
    
    image_maze(axis, maze)

    def update(frame_id: int):
        nonlocal x_points, y_points
        if frame_id == 0:
            x_points = np.append(x_points, start[1])
            y_points = np.append(y_points, start[0])
        else:
            mask_cells = visited_cells == frame_id
            cells = np.nonzero(mask_cells)

            x_points = np.append(x_points, cells[1])
            y_points = np.append(y_points, cells[0])

        if frame_id == visited_cells[*end]:
            end_point.set_data([end[1]], [end[0]])
        else:
            end_point.set_data([], [])

        wave.set_data(x_points, y_points)
        return wave, end_point

    animation = FuncAnimation(figure, update, frames=np.max(visited_cells) + 1, interval=200)

    if save_path:
        animation.save(save_path, writer="pillow", fps=3)
    return animation


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
    save_path = "labyrinth.gif"  # Укажите путь для сохранения анимации

    animation = animate_wave_algorithm(maze, start, end, save_path)
    HTML(animation.to_jshtml())

    # Пример 2

    maze_path = "solutions\sem02\lesson08\data\maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (3, 6)
    end = (98, 33)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())