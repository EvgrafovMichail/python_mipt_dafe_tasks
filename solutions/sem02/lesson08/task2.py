from collections import deque
from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def update(frame, waves, path, scat, path_line):
    if frame < len(waves):
        cells = waves[frame]
        x = [c[1] for c in cells]
        y = [c[0] for c in cells]
        scat.set_offsets(np.c_[x, y])
        return (scat,)

    else:
        scat.set_offsets(np.empty((0, 2)))
        if path:
            px = [c[1] for c in path]
            py = [c[0] for c in path]
            path_line.set_data(px, py)
        return (scat, path_line)


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    rows, cols = maze.shape

    dist = np.full((rows, cols), -1)
    dist[start] = 0
    queue = deque([start])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    waves = [[start]]

    while queue and dist[end] == -1:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 1 and dist[nr, nc] == -1:
                dist[nr, nc] = dist[r, c] + 1
                queue.append((nr, nc))

                current_dist = dist[nr, nc]
                if len(waves) <= current_dist:
                    waves.append([])
                waves[current_dist].append((nr, nc))

    path = []
    if dist[end] != -1:
        r, c = end
        while (r, c) != start:
            path.append((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr, nc] == dist[r, c] - 1:
                    r, c = nr, nc
                    break
        path.append(start)
        path.reverse()

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(maze, cmap="gray", origin="upper")

    scat = ax.scatter([], [], c="yellow", s=150, zorder=3)
    (path_line,) = ax.plot([], [], c="red", lw=3, zorder=4)

    ax.scatter(start[1], start[0], c="green", s=200, label="Start")
    ax.scatter(end[1], end[0], c="blue", s=200, label="End")

    bound_update = partial(update, waves=waves, path=path, scat=scat, path_line=path_line)

    animation = FuncAnimation(fig, bound_update, frames=len(waves) + 1, interval=150, blit=True)

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
