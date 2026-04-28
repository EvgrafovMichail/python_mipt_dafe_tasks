from collections import deque

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def wave_algorithm(maze, start, end):
    rows, cols = maze.shape
    dist = np.full((rows, cols), -1, dtype=int)
    dist[start] = 0
    frames = [dist.copy()]
    q = deque([start])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 1 and dist[nr, nc] == -1:
                dist[nr, nc] = dist[r, c] + 1
                frames.append(dist.copy())
                if (nr, nc) == end:
                    return dist, frames
                q.append((nr, nc))
    return dist, frames


def reconstruct_path(dist, start, end):
    if dist[end] == -1:
        return []
    path = [end]
    r, c = end
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while (r, c) != start:
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < dist.shape[0]
                and 0 <= nc < dist.shape[1]
                and dist[nr, nc] == dist[r, c] - 1
            ):
                path.append((nr, nc))
                r, c = nr, nc
                break
    return path[::-1]


def animate_wave_algorithm(maze, start, end, save_path=""):
    dist, bfs_frames = wave_algorithm(maze, start, end)
    path = reconstruct_path(dist, start, end)

    if not path:
        print("Сообщение: Путь не существует")

    frames = [(d, []) for d in bfs_frames]
    if path:
        for i in range(1, len(path) + 1):
            frames.append((bfs_frames[-1], path[:i]))

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks(range(maze.shape[1]))
    ax.set_yticks(range(maze.shape[0]))
    ax.imshow(maze == 0, cmap="gray_r", alpha=0.5)
    max_dist = dist.max() if dist.max() > 0 else 1
    im = ax.imshow(np.zeros_like(maze), cmap="viridis", vmin=0, vmax=max_dist, alpha=0.6)
    texts = [
        [ax.text(j, i, "", ha="center", va="center", fontsize=8) for j in range(maze.shape[1])]
        for i in range(maze.shape[0])
    ]
    ax.scatter(start[1], start[0], c="lime", s=100, edgecolors="black", marker="o", label="Начало")
    ax.scatter(end[1], end[0], c="red", s=100, edgecolors="black", marker="*", label="Конец")
    (line,) = ax.plot([], [], "cyan", linewidth=3, label="Путь")

    if not path:
        ax.text(
            0.5,
            0.5,
            "Путь не существует",
            transform=ax.transAxes,
            ha="center",
            va="center",
            fontsize=16,
            color="red",
            bbox=dict(facecolor="white", alpha=0.8),
        )

    ax.legend()

    def update(idx):
        d, p = frames[idx]
        show = np.where(maze == 0, np.nan, d.astype(float))
        im.set_array(show)
        for i in range(maze.shape[0]):
            for j in range(maze.shape[1]):
                if maze[i, j] == 1 and d[i, j] != -1:
                    texts[i][j].set_text(str(d[i, j]))
                else:
                    texts[i][j].set_text("")
        if p:
            y, x = zip(*p)
            line.set_data(x, y)
        else:
            line.set_data([], [])
        return [im, line] + [
            texts[i][j] for i in range(maze.shape[0]) for j in range(maze.shape[1])
        ]

    anim = FuncAnimation(fig, update, frames=len(frames), interval=200, blit=False)
    if save_path:
        anim.save(save_path, writer="pillow", fps=5)
    return anim


if __name__ == "__main__":
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
    anim = animate_wave_algorithm(maze, start, end, "labyrinth.gif")
    HTML(anim.to_jshtml())
