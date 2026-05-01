from functools import partial
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

plt.rcParams["animation.embed_limit"] = 50.0


def calculate_wave_data(
    maze: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]
) -> Tuple[List[np.ndarray], List[Tuple[int, int]], float]:
    """Выполняет поиск кратчайшего пути и подготавливает данные для кадров."""
    rows, cols = maze.shape
    distances = np.full((rows, cols), np.nan)
    distances[maze == 0] = -1.0

    queue = [start]
    distances[start] = 0.0
    frames_data = [distances.copy()]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    found = False

    while queue:
        next_queue = []
        for r, c in queue:
            if (r, c) == end:
                found = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if maze[nr, nc] == 1 and np.isnan(distances[nr, nc]):
                        distances[nr, nc] = distances[r, c] + 1.0
                        next_queue.append((nr, nc))

        frames_data.append(distances.copy())
        if found:
            break
        queue = next_queue

    max_dist = np.nanmax(distances) if not np.isnan(np.nanmax(distances)) else 0.0

    path = []
    if distances[end] >= 0:
        curr = end
        path.append(curr)
        curr_dist = distances[end]
        while curr != start:
            r, c = curr
            moved = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if distances[nr, nc] == curr_dist - 1.0:
                        curr = (nr, nc)
                        path.append(curr)
                        curr_dist -= 1.0
                        moved = True
                        break
            if not moved:
                break
        path.reverse()

    if path:
        path_val = max_dist + 1.0
        final_state = distances.copy()
        for r, c in path:
            final_state[r, c] = path_val
            frames_data.append(final_state.copy())

    return frames_data, path, max_dist


def create_canvas(
    is_path_found: bool, initial_frame: np.ndarray, max_dist: float
) -> Tuple[plt.Figure, plt.Axes, plt.AxesImage]:
    """Создает полотно и инициализирует объект изображения."""
    figure, axis = plt.subplots(figsize=(6, 6))
    axis.set_xticks([])
    axis.set_yticks([])
    axis.set_title("Волновой алгоритм (Алгоритм Ли)" if is_path_found else "Путь не найден")

    cmap = plt.get_cmap("viridis").copy()
    cmap.set_under("black")
    cmap.set_over("red")
    cmap.set_bad("white")

    vmax = max(max_dist, 1.0)
    image = axis.imshow(initial_frame, cmap=cmap, vmin=0, vmax=vmax)

    return figure, axis, image


def update_frame(
    frame_idx: int, image: plt.AxesImage, frames_data: List[np.ndarray]
) -> Tuple[plt.AxesImage]:
    """Обновляет матрицу данных изображения на каждом шаге."""
    image.set_array(frames_data[frame_idx])
    return (image,)


def build_animation(
    figure: plt.Figure, image: plt.AxesImage, frames_data: List[np.ndarray], interval: int = 150
) -> FuncAnimation:
    """Создает объект анимации FuncAnimation."""
    frame_updater = partial(update_frame, image=image, frames_data=frames_data)

    return FuncAnimation(
        figure, frame_updater, frames=len(frames_data), interval=interval, blit=True
    )


def save_animation_to_file(animation: FuncAnimation, save_path: str) -> None:
    """Сохраняет анимацию в формате GIF."""
    if save_path:
        animation.save(save_path, writer="pillow")


def animate_wave_algorithm(
    maze: np.ndarray, start: Tuple[int, int], end: Tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    """Оркестратор: координирует расчеты, создание визуализации и сохранение."""
    frames_data, path, max_dist = calculate_wave_data(maze, start, end)

    figure, axis, image = create_canvas(len(path) > 0, frames_data[0], max_dist)

    animation = build_animation(figure, image, frames_data)

    if save_path:
        save_animation_to_file(animation, save_path)

    plt.close(figure)
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

    # можете поменять, если захотите запустить из других точек
    start = (2, 0)
    end = (5, 0)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
