import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def mark_cells(visited_cells, start_x, start_y):
    if (
        start_x < 0
        or start_x >= visited_cells.shape[0]
        or start_y < 0
        or start_y >= visited_cells.shape[1]
    ):
        print("Начальная точка находится за пределами лабиринта")
        return
    if visited_cells[start_x, start_y] != -1:
        print("Начальная точка находится в стене")
        return

    step = 0
    cells = [(start_x, start_y, step)]
    current = 0

    while current < len(cells):
        x, y, step = cells[current]
        current += 1

        # проверяем текущую клетку
        if x < 0 or x >= visited_cells.shape[0] or y < 0 or y >= visited_cells.shape[1]:
            continue

        if visited_cells[x, y] != -1:
            continue

        visited_cells[x, y] = step

        cells.append((x + 1, y, step + 1))
        cells.append((x - 1, y, step + 1))
        cells.append((x, y + 1, step + 1))
        cells.append((x, y - 1, step + 1))


def is_there_way_out(visited_cells, end):
    if visited_cells[end] == -1:
        print("Пути до выхода не существует")


def image_maze(axis, maze):
    x_size, y_size = maze.shape[1], maze.shape[0]
    axis.set_title("Волновой алгоритм", fontsize=17, fontweight="bold")

    axis.set_xticks(np.arange(0, x_size, max(1, x_size // 10)))
    axis.set_yticks(np.arange(0, y_size, max(1, y_size // 10)))

    axis.set_xticks(np.arange(-0.5, x_size, 1), minor=True)
    axis.set_yticks(np.arange(-0.5, y_size, 1), minor=True)

    axis.tick_params(axis="both", which="major", labelsize=12, width=3)

    axis.grid(True, which="minor", linewidth=2, color="black", alpha=1)
    axis.grid(False, which="major")

    axis.set_xlim(-0.5, x_size - 0.5)
    axis.set_ylim(y_size - 0.5, -0.5)

    # окрашиваем путь лабиринта
    way_mask = maze != 0
    way = np.zeros((maze.shape[0], maze.shape[1], 4))
    way[way_mask] = [0, 0, 0, 1]  # черный цвет для пути

    axis.imshow(way, extent=[-0.5, x_size - 0.5, y_size - 0.5, -0.5], origin="upper", alpha=1)


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    visited_cells = -1 * maze.astype(np.int32)

    mark_cells(visited_cells, *start)
    is_there_way_out(visited_cells, end)

    figure, axis = plt.subplots(figsize=(10, 10))

    m_size = 500 / max(*maze.shape)  # размер маркера
    x_points, y_points = np.array([]), np.array([])
    wave, *_ = axis.plot(x_points, y_points, "o", ms=m_size)
    end_point, *_ = axis.plot([], [], "o", ms=m_size, c="green")

    image_maze(axis, maze)  # изображаем сам лабиринт

    def update(frame_id):
        nonlocal x_points, y_points
        if frame_id == 0:
            x_points = np.append(x_points, start[1])
            y_points = np.append(y_points, start[0])
        else:
            cells = np.where(visited_cells == frame_id)

            new_x = cells[1]
            new_y = cells[0]

            x_points = np.append(x_points, new_x)
            y_points = np.append(y_points, new_y)

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
    start = (30, 4)
    end = (100, 43)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
