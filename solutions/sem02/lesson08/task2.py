from collections import deque

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    h, w = maze.shape

    dist = np.full((h, w), -1)
    dist[start] = 0
    q = deque([start])

    waves = []
    path_steps = []
    found = False

    while q and not found:
        waves.append(dist.copy())
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) == end:
                found = True
                break
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and maze[nx, ny] == 1 and dist[nx, ny] == -1:
                    dist[nx, ny] = dist[x, y] + 1
                    q.append((nx, ny))
    waves.append(dist.copy())

    if found:
        path = [end]
        x, y = end
        while (x, y) != start:
            cur = dist[x, y]
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and dist[nx, ny] == cur - 1:
                    x, y = nx, ny
                    path.append((x, y))
                    break
        path.reverse()
        for i in range(1, len(path) + 1):
            path_steps.append(path[:i])

    fig, ax = plt.subplots(figsize=(8, 8))

    colors = {
        "wall": [0.3, 0.2, 0.2],
        "path": [0.95, 0.95, 0.95],
        "start": [0.2, 0.8, 0.2],
        "end": [0.8, 0.2, 0.2],
        "wave": [0.3, 0.6, 0.9],
        "route": [1.0, 0.8, 0.2],
    }

    img = np.zeros((h, w, 3))
    for i in range(h):
        for j in range(w):
            img[i, j] = colors["wall"] if maze[i, j] == 0 else colors["path"]
    img[start] = colors["start"]
    img[end] = colors["end"]

    im = ax.imshow(img, interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])

    def update(frame):
        cur_img = img.copy()

        if frame < len(waves):
            wav = waves[frame]
            for i in range(h):
                for j in range(w):
                    if wav[i, j] >= 0 and maze[i, j] == 1 and (i, j) != start and (i, j) != end:
                        cur_img[i, j] = colors["wave"]

        else:
            idx = frame - len(waves)
            if idx < len(path_steps):
                for x, y in path_steps[idx]:
                    if (x, y) != start and (x, y) != end:
                        cur_img[x, y] = colors["route"]

        im.set_array(cur_img)
        return (im,)

    total = len(waves) + len(path_steps)
    anim = FuncAnimation(fig, update, frames=total if total > 0 else 1, interval=100, repeat=False)

    if save_path:
        anim.save(save_path, writer="pillow", fps=10)

    plt.close(fig)
    return anim


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
