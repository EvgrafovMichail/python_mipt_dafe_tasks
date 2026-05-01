from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

WALL_VALUE = -2
UNVISITED_VALUE = -1
PATH_VALUE = 1


def get_neighbours(
    cell: tuple[int, int],
    shape: tuple[int, int],
) -> list[tuple[int, int]]:
    row, col = cell
    rows, cols = shape
    neighbours: list[tuple[int, int]] = []

    if row > 0:
        neighbours.append((row - 1, col))
    if row + 1 < rows:
        neighbours.append((row + 1, col))
    if col > 0:
        neighbours.append((row, col - 1))
    if col + 1 < cols:
        neighbours.append((row, col + 1))

    return neighbours


def validate_points(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
) -> None:
    rows, cols = maze.shape
    start_row, start_col = start
    end_row, end_col = end

    if not (0 <= start_row < rows and 0 <= start_col < cols):
        raise ValueError("start point is out of maze bounds")
    if not (0 <= end_row < rows and 0 <= end_col < cols):
        raise ValueError("end point is out of maze bounds")
    if maze[start] == 0:
        raise ValueError("start point must be on a free cell")
    if maze[end] == 0:
        raise ValueError("end point must be on a free cell")


def run_wave_algorithm(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[list[np.ndarray], np.ndarray]:
    distances = np.full(maze.shape, UNVISITED_VALUE, dtype=int)
    distances[maze == 0] = WALL_VALUE
    wave_frames: list[np.ndarray] = []

    frontier = [start]
    distances[start] = 0
    wave_frames.append(distances.astype(float).copy())

    while frontier and distances[end] == UNVISITED_VALUE:
        next_frontier: list[tuple[int, int]] = []

        for cell in frontier:
            for neighbour in get_neighbours(cell, maze.shape):
                row, col = neighbour
                if distances[row, col] != UNVISITED_VALUE:
                    continue

                distances[row, col] = distances[cell] + 1
                next_frontier.append(neighbour)

        if not next_frontier:
            break

        wave_frames.append(distances.astype(float).copy())
        frontier = next_frontier

    return wave_frames, distances


def build_reverse_path(
    distances: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
) -> list[tuple[int, int]]:
    if distances[end] < 0:
        return []

    path = [end]
    current = end

    while current != start:
        for neighbour in get_neighbours(current, distances.shape):
            if distances[neighbour] == distances[current] - 1:
                current = neighbour
                path.append(current)
                break

    return path


def create_path_frames(
    path: list[tuple[int, int]],
    shape: tuple[int, int],
) -> list[np.ndarray]:
    if not path:
        return []

    path_frames: list[np.ndarray] = []

    for path_end in range(1, len(path) + 1):
        frame = np.zeros(shape, dtype=float)
        for row, col in path[:path_end]:
            frame[row, col] = PATH_VALUE
        path_frames.append(frame)

    return path_frames


def create_point_frame(
    point: tuple[int, int],
    shape: tuple[int, int],
) -> np.ndarray:
    frame = np.zeros(shape, dtype=float)
    frame[point] = 1
    return frame


def create_alpha_mask(
    frame: np.ndarray,
    threshold: float,
    alpha_value: float = 1.0,
) -> np.ndarray:
    alpha = np.zeros(frame.shape, dtype=float)
    alpha[frame >= threshold] = alpha_value
    return alpha


def update_frame(
    frame_id: int,
    *,
    wave_image,
    path_image,
    wave_frames: list[np.ndarray],
    path_frames: list[np.ndarray],
) -> tuple:
    if frame_id < len(wave_frames):
        current_wave = wave_frames[frame_id]
        current_path = np.zeros_like(current_wave, dtype=float)
    else:
        current_wave = wave_frames[-1]
        current_path = path_frames[frame_id - len(wave_frames)]

    wave_image.set_data(np.where(current_wave >= 0, current_wave, 0))
    wave_image.set_alpha(create_alpha_mask(current_wave, 0, 0.95))
    path_image.set_data(current_path)
    path_image.set_alpha(create_alpha_mask(current_path, 1))
    return wave_image, path_image


def animate_wave_algorithm(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
    save_path: str = "",
) -> FuncAnimation:
    validate_points(maze, start, end)

    wave_frames, distances = run_wave_algorithm(maze, start, end)
    path = build_reverse_path(distances, start, end)
    path_frames = create_path_frames(path, maze.shape)
    wave_max_value = max(float(distances.max()), 1.0)

    figure, axis = plt.subplots(figsize=(9, 9))

    free_frame = maze * 0.75
    wall_frame = (maze == 0).astype(float)
    start_frame = create_point_frame(start, maze.shape)
    end_frame = create_point_frame(end, maze.shape)

    axis.imshow(
        free_frame,
        origin="lower",
        cmap="Blues",
        vmin=0,
        vmax=1,
        alpha=create_alpha_mask(free_frame, 0.1),
    )
    axis.imshow(
        wall_frame,
        origin="lower",
        cmap="Blues",
        vmin=0,
        vmax=1,
        alpha=create_alpha_mask(wall_frame, 1),
    )
    wave_image = axis.imshow(
        np.where(wave_frames[0] >= 0, wave_frames[0], 0),
        origin="lower",
        cmap="YlGn",
        vmin=0,
        vmax=wave_max_value,
        alpha=create_alpha_mask(wave_frames[0], 0, 0.95),
    )
    path_image = axis.imshow(
        np.zeros_like(maze, dtype=float),
        origin="lower",
        cmap="Reds",
        vmin=0,
        vmax=1,
        alpha=np.zeros(maze.shape, dtype=float),
    )
    axis.imshow(
        start_frame,
        origin="lower",
        cmap="YlGn",
        vmin=0,
        vmax=1,
        alpha=create_alpha_mask(start_frame, 1),
    )
    axis.imshow(
        end_frame,
        origin="lower",
        cmap="Reds",
        vmin=0,
        vmax=1,
        alpha=create_alpha_mask(end_frame, 1),
    )

    axis.axis("image")
    axis.grid(False)
    figure.colorbar(wave_image, ax=axis)

    animation = FuncAnimation(
        figure,
        partial(
            update_frame,
            wave_image=wave_image,
            path_image=path_image,
            wave_frames=wave_frames,
            path_frames=path_frames,
        ),
        frames=len(wave_frames) + len(path_frames),
        interval=300,
        blit=True,
    )

    if save_path != "":
        animation.save(save_path, writer="pillow", fps=24)

    if not path:
        print("Путь от старта до финиша не найден")

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
    save_path = "labyrinth.gif"

    animation = animate_wave_algorithm(maze, start, end, save_path)
    HTML(animation.to_jshtml())

    # Пример 2
    maze_path = "./data/maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (0, 18)
    end = (101, 43)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(
        loaded_maze,
        start,
        end,
        loaded_save_path,
    )
    HTML(loaded_animation.to_jshtml())
