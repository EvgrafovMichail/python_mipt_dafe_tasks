from collections import deque

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def wave_propagation(maze: np.ndarray, start: tuple[int, int]):
    rows, cols = maze.shape
    dist = np.full((rows, cols), -1, dtype=int)

    queue = deque()
    queue.append(start)
    dist[start] = 0
    frames = [dist.copy()]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr, nc] == 1 and dist[nr, nc] == -1:
                    dist[nr, nc] = dist[r, c] + 1
                    queue.append((nr, nc))
                    frames.append(dist.copy())

    return dist, frames


def restore_path(dist: np.ndarray, start: tuple[int, int], end: tuple[int, int]):
    if dist[end] == -1:
        return []

    path = [end]
    cur = end
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while cur != start:
        r, c = cur
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < dist.shape[0] and 0 <= nc < dist.shape[1]:
                if dist[nr, nc] == dist[r, c] - 1:
                    cur = (nr, nc)
                    path.append(cur)
                    break

    return path.reverse()


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    dist, frames = wave_propagation(maze, start)
    path = restore_path(dist, start, end)

    frames_path = []
    if path:
        temp = dist.copy()
        for r, c in path:
            temp[r, c] = temp.max() + 2
            frames_path.append(temp.copy())

    all_frames = frames + frames_path

    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.set_title("Волновой алгоритм")

        display = np.where(maze == 0, -2, frame)

        im = ax.imshow(display)

        ax.scatter(start[1], start[0], c="green", s=10, label="Start")
        ax.scatter(end[1], end[0], c="red", s=10, label="End")

        ax.legend()

        return [im]

    animation = FuncAnimation(fig, update, frames=all_frames, interval=200, repeat=False)

    if save_path:
        animation.save(save_path, writer="pillow")

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

    # Пример 2
    maze_path = "solutions/sem02/lesson08/data/maze.npy"
    loaded_maze = np.load(maze_path)

    start = (2, 0)
    end = (5, 0)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
