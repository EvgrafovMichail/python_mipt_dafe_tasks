from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation


from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def run_wave(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[list[np.ndarray], list[tuple[int, int]]]:
    rows, cols = maze.shape
    wave = maze.astype(float) - 2
    wave[start] = 0

    frames = [wave.copy()]
    frontier = [start]
    found = False

    while frontier and not found:
        next_frontier = []
        for r, c in frontier:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and wave[nr, nc] == -1:
                    wave[nr, nc] = wave[r, c] + 1
                    next_frontier.append((nr, nc))
                    if (nr, nc) == end:
                        found = True
        frontier = next_frontier
        frames.append(wave.copy())

    path = backtrack(wave, start, end) if found else []
    return frames, path


def backtrack(
    wave: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
) -> list[tuple[int, int]]:
    path = [end]
    r, c = end

    while (r, c) != start:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < wave.shape[0]
                and 0 <= nc < wave.shape[1]
                and wave[nr, nc] == wave[r, c] - 1
            ):
                path.append((nr, nc))
                r, c = nr, nc
                break

    return path


def build_overlay(
    maze: np.ndarray,
    frame: np.ndarray,
    path: list[tuple[int, int]],
    path_length: int,
    path_value: float,
) -> np.ndarray:
    overlay = np.full(maze.shape, np.nan)

    wave_mask = frame >= 0
    overlay[wave_mask] = frame[wave_mask]

    for r, c in path[:path_length]:
        overlay[r, c] = path_value

    return overlay


def update_frame(
    frame_id: int,
    *,
    maze: np.ndarray,
    base_image,
    overlay_image,
    frames: list[np.ndarray],
    path: list[tuple[int, int]],
    path_value: float,
) -> tuple:
    wave_count = len(frames)

    if frame_id < wave_count:
        current_wave = frames[frame_id]
        path_length = 0
    else:
        current_wave = frames[-1]
        path_length = frame_id - wave_count + 1

    overlay = build_overlay(
        maze=maze,
        frame=current_wave,
        path=path,
        path_length=path_length,
        path_value=path_value,
    )

    base_image.set_data(maze)
    overlay_image.set_data(overlay)
    return base_image, overlay_image


def animate_wave_algorithm(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
    save_path: str = "",
) -> FuncAnimation:
    frames, path = run_wave(maze, start, end)

    if not path:
        print("Путь не существует")

    last_wave = frames[-1]
    max_wave = last_wave[last_wave >= 0].max() if (last_wave >= 0).any() else 1.0
    path_value = max_wave + 5

    figure, axis = plt.subplots(figsize=(9, 9))
    axis.grid(False)

    base_image = axis.imshow(
        maze,
        cmap="gray",
        vmin=0,
        vmax=1,
        origin="upper",
    )

    overlay_cmap = plt.cm.hot.copy()
    overlay_cmap.set_bad(alpha=0)

    first_overlay = build_overlay(
        maze=maze,
        frame=frames[0],
        path=path,
        path_length=0,
        path_value=path_value,
    )

    overlay_image = axis.imshow(
        first_overlay,
        cmap=overlay_cmap,
        vmin=0,
        vmax=path_value,
        origin="upper",
        alpha=0.9,
    )

    axis.axis("image")

    animation = FuncAnimation(
        figure,
        partial(
            update_frame,
            maze=maze,
            base_image=base_image,
            overlay_image=overlay_image,
            frames=frames,
            path=path,
            path_value=path_value,
        ),
        frames=len(frames) + len(path),
        interval=100,
        blit=False,
    )

    if save_path:
        animation.save(save_path, writer="pillow", fps=10)

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

    maze_path = "solutions/sem02/lesson08/data/maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (0, 17)
    end = (101, 43)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
