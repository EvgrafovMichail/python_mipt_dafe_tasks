from collections import deque
from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def get_frames_and_path(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[list, list | None]:
    current_frame = np.zeros(maze.shape, dtype=int) - 1
    frames = [current_frame.copy()]

    current_frame[*start] = 0
    frames.append(current_frame.copy())
    queue = deque()
    queue.append(start)
    variants = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    path = None

    while queue:
        x, y = queue.popleft()
        for var in variants:
            new_x = x + var[0]
            new_y = y + var[1]

            if (
                0 <= new_x < maze.shape[0]
                and 0 <= new_y < maze.shape[1]
                and maze[new_x, new_y]
                and current_frame[new_x, new_y] == -1
            ):
                current_frame[new_x, new_y] = current_frame[x, y] + 1
                frames.append(current_frame.copy())
                queue.append((new_x, new_y))

                if (new_x, new_y) == end:
                    path = [end]
                    last = end

                    while last != start:
                        for last_var in variants:
                            prev_x = last[0] + last_var[0]
                            prev_y = last[1] + last_var[1]
                            if (
                                0 <= prev_x < maze.shape[0]
                                and 0 <= prev_y < maze.shape[1]
                                and current_frame[prev_x, prev_y] == current_frame[*last] - 1 != -1
                            ):
                                last = (prev_x, prev_y)
                                path.append(last)
                                break

    return frames, path


def update_frame(
    frame_id: int,
    maze: np.ndarray,
    frames: list[np.ndarray],
    path: list | None,
    start: tuple[int, int],
    end: tuple[int, int],
    axis: plt.Axes,
) -> tuple[plt.Axes]:
    axis.clear()
    image = np.zeros((*maze.shape, 3))
    image[maze == 0] = [0, 0, 0]
    image[maze == 1] = [255, 255, 255]

    current_frame = frames[min(len(frames) - 1, frame_id)]
    image[current_frame >= 0] = [0, 120, 0]

    if path and frame_id >= len(frames) - 1:
        for ceil in path:
            image[*ceil] = [0, 255, 0]

    image[*start] = [120, 0, 120]
    image[*end] = [255, 0, 0]

    axis.imshow(image / 255)
    axis.set_xticks(range(maze.shape[1]))
    axis.set_yticks(range(maze.shape[0]))
    return (axis,)


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    frames, path = get_frames_and_path(maze, start, end)
    figure, axis = plt.subplots(figsize=(8, 8))

    update_function = partial(
        update_frame, maze=maze, frames=frames, path=path, start=start, end=end, axis=axis
    )

    animation = FuncAnimation(
        figure,
        update_function,
        frames=len(frames),
        interval=2000,
        blit=False,
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
