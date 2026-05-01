from functools import partial
from typing import List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from matplotlib.collections import PathCollection


class WaveAlgorithm:
    matrix_: np.ndarray
    path: Optional[List[List[int]]]
    wave_front_history: List[List[List[int]]]

    def __init__(self, matrix: np.ndarray):
        self.matrix_ = matrix.T
        self.path = None
        self.wave_front_history = []

    def process(self, start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[List[int]]]:
        start_ = [start[1], start[0]]
        end_ = [end[1], end[0]]

        distances = np.zeros(shape=self.matrix_.shape) - 1
        distances[tuple(start_)] = 0
        current_wave_front = [start_]

        self.wave_front_history = [[start_]]

        current_distance = 0
        while current_wave_front:
            current_distance += 1
            next_wave_front = []

            for point in current_wave_front:
                for neighbor in self._get_neighbors(point):
                    if self.matrix_[tuple(neighbor)] == 1 and distances[tuple(neighbor)] == -1:
                        distances[tuple(neighbor)] = current_distance
                        next_wave_front.append(neighbor)

                        if neighbor == end_:
                            self.wave_front_history.append([end_])
                            self._find_path(distances, start_, end_)
                            return self.path, self.wave_front_history

            if next_wave_front:
                self.wave_front_history.append(next_wave_front)

            current_wave_front = next_wave_front

        return self.path, self.wave_front_history

    def _get_neighbors(self, point: List[int]) -> List[List[int]]:
        x_max, y_max = self.matrix_.shape
        x, y = point
        neighbors = []

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + dx < x_max and 0 <= y + dy < y_max:
                neighbors.append([x + dx, y + dy])

        return neighbors

    def _find_path(self, distances: np.ndarray, start: List[int], end: List[int]) -> None:
        path = [end]
        current_point = end

        while current_point != start:
            current_distance = distances[tuple(current_point)]
            found = False

            for neighbor in self._get_neighbors(current_point):
                if distances[tuple(neighbor)] == current_distance - 1:
                    path.append(neighbor)
                    current_point = neighbor
                    found = True
                    break

            if not found:
                return

        path.reverse()
        self.path = path


def create_plot(maze: np.ndarray):
    figure, axis = plt.subplots(figsize=(10, 9))
    axis.imshow(maze, cmap="gray")
    return figure, axis


def update_frame(
    frame: int,
    scatter: PathCollection,
    path: List[Tuple[int, int]],
    wave_front_history: List[List[Tuple[int, int]]],
) -> None:
    points = []
    for i in range(frame + 1):
        points.extend(wave_front_history[i])

    scatter.set_offsets(points)


def style_axis(axis: Axes):
    axis.set_title("Волновой алгоритм")


def is_valid_point(point: Tuple[int, int], matrix: np.ndarray):
    return 0 <= point[0] < matrix.shape[0] and 0 <= point[1] < matrix.shape[1]


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    if not (is_valid_point(start, maze) and is_valid_point(start, maze)):
        raise ValueError("Точка старта или выхода выходит за границу")

    if maze[start] == 0 or maze[end] == 0:
        print("Невозможно найти путь. Старт или выход находятся на стене")

    wave_algorithm = WaveAlgorithm(maze)
    path, wave_front_history = wave_algorithm.process(start, end)

    if path is None:
        print("Не удалось найти путь")
        return

    figure, axis = create_plot(maze)
    style_axis(axis)
    scatter = axis.scatter([], [], s=140)

    animation = FuncAnimation(
        figure,
        partial(update_frame, scatter=scatter, path=path, wave_front_history=wave_front_history),
        frames=len(wave_front_history),
        interval=300,
    )

    if save_path:
        animation.save(save_path)

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

    maze_path = "./data/maze.npy"
    loaded_maze = np.load(maze_path)

    # # можете поменять, если захотите запустить из других точек
    start = (30, 4)
    end = (100, 43)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
