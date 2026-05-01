from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def _is_inside(maze: np.ndarray, row: int, col: int) -> bool:
    return 0 <= row < maze.shape[0] and 0 <= col < maze.shape[1]


def _neighbors(row: int, col: int) -> list[tuple[int, int]]:
    return [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
    ]


def _run_wave_algorithm(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[np.ndarray, list[list[tuple[int, int]]], list[tuple[int, int]]]:
    distances = np.full(maze.shape, -1, dtype=int)

    start_row, start_col = start
    end_row, end_col = end

    distances[start_row, start_col] = 0
    wave_layers = [[start]]
    current_layer = [start]

    found = start == end
    distance_value = 0

    while current_layer and not found:
        next_layer = []
        distance_value += 1

        for row, col in current_layer:
            for next_row, next_col in _neighbors(row, col):
                if not _is_inside(maze, next_row, next_col):
                    continue
                if maze[next_row, next_col] == 0:
                    continue
                if distances[next_row, next_col] != -1:
                    continue

                distances[next_row, next_col] = distance_value
                next_layer.append((next_row, next_col))

                if (next_row, next_col) == end:
                    found = True

        if next_layer:
            wave_layers.append(next_layer)
        current_layer = next_layer

    path: list[tuple[int, int]] = []
    if distances[end_row, end_col] != -1:
        current = end
        path = [current]

        while current != start:
            row, col = current
            for next_row, next_col in _neighbors(row, col):
                if not _is_inside(maze, next_row, next_col):
                    continue
                if distances[next_row, next_col] == distances[row, col] - 1:
                    current = (next_row, next_col)
                    path.append(current)
                    break

        path.reverse()

    return distances, wave_layers, path


def _build_animation_frames(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
    wave_layers: list[list[tuple[int, int]]],
    path: list[tuple[int, int]],
) -> list[np.ndarray]:
    state = np.where(maze == 0, 0, 1).astype(int)
    frames = [state.copy()]

    state[start] = 2
    state[end] = 3
    frames.append(state.copy())

    for layer in wave_layers[1:]:
        for row, col in layer:
            if (row, col) not in (start, end):
                state[row, col] = 4
        state[start] = 2
        state[end] = 3
        frames.append(state.copy())

    for row, col in path:
        if (row, col) not in (start, end):
            state[row, col] = 5
        state[start] = 2
        state[end] = 3
        frames.append(state.copy())

    return frames


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    # ваш код
    if maze.ndim != 2:
        raise ValueError()

    if not _is_inside(maze, *start) or not _is_inside(maze, *end):
        raise ValueError()

    if maze[start] == 0 or maze[end] == 0:
        raise ValueError()

    _, wave_layers, path = _run_wave_algorithm(maze, start, end)
    frames = _build_animation_frames(maze, start, end, wave_layers, path)

    figure, axis = plt.subplots(figsize=(7, 7))
    axis: plt.Axes

    color_map = plt.matplotlib.colors.ListedColormap(
        [
            "#1e1e1e",  # стена
            "#f5f5f5",  # проход
            "#4caf50",  # старт
            "#e53935",  # финиш
            "#42a5f5",  # волна
            "#ffd54f",  # путь
        ]
    )

    image = axis.imshow(frames[0], cmap=color_map, vmin=0, vmax=5)
    axis.set_title("Волновой алгоритм")
    axis.set_xticks([])
    axis.set_yticks([])

    path_exists = len(path) > 0

    def update(frame_id: int):
        image.set_data(frames[frame_id])
        if frame_id < 2:
            axis.set_title("Подготовка")
        elif frame_id < len(frames) - (1 if path_exists else 0):
            axis.set_title("Распространение волны")
        elif path_exists:
            axis.set_title("Восстановление кратчайшего пути")
        else:
            axis.set_title("Путь не существует")
        return [image]

    animation = FuncAnimation(
        figure,
        update,
        frames=len(frames),
        interval=250,
        blit=True,
    )

    if save_path:
        animation.save(save_path, writer="pillow", fps=5)

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
    save_path = "solutions/sem02/lesson08/labyrinth.gif"  # Укажите путь для сохранения анимации

    animation = animate_wave_algorithm(maze, start, end, save_path)
    HTML(animation.to_jshtml())

    # Пример 2

    maze_path = Path(__file__).parent / "data" / "maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (2, 0)
    end = (5, 0)
    if loaded_maze[start] == 0 or loaded_maze[end] == 0:
        passable_cells = np.argwhere(loaded_maze == 1)
        if len(passable_cells) < 2:
            raise ValueError()
        start = tuple(passable_cells[0])
        end = tuple(passable_cells[-1])
    loaded_save_path = "solutions/sem02/lesson08/loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
