from functools import partial

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def update(rows, cols, texts, frame):
    new = []

    for i in range(rows):
        for j in range(cols):
            if frame[i, j] >= 0:
                new_text = str(int(frame[i, j]))
            else:
                new_text = ""

            if texts[i][j].get_text() != new_text:
                texts[i][j].set_text(new_text)
                new.append(texts[i][j])

    return new


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:

    rows, cols = maze.shape
    dist = np.full((rows, cols), -1)
    frames = []

    dist[start] = 0
    now_front = [start]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    step = 0

    while now_front:
        frames.append(dist.copy())
        next_front = []

        for x, y in now_front:
            if (x, y) == end:
                now_front = []
                break

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 1 and dist[nx, ny] == -1:
                    dist[nx, ny] = step + 1
                    next_front.append((nx, ny))

        now_front = next_front
        step += 1

    path = []
    if dist[end] != -1:
        c = end
        path.append(c)

        while c != start:
            x, y = c
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and dist[nx, ny] == dist[x, y] - 1:
                    c = (nx, ny)
                    path.append(c)
                    break
        path.reverse()

    if path:
        final = dist.copy()
        for x, y in path:
            final[x, y] = np.max(final) + 2
        frames.append(final)

    fig, ax = plt.subplots()

    base = np.zeros_like(maze, dtype=float)
    base[maze == 0] = 1

    img = ax.imshow(base, cmap="gray")

    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which="minor", color="black", linewidth=2)

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title("Волновой алгоритм")

    texts = []
    for i in range(rows):
        row = []
        for j in range(cols):
            t = ax.text(j, i, "", color="blue", fontsize=14, fontweight="bold")
            row.append(t)
        texts.append(row)

    animation = FuncAnimation(
        fig,
        partial(update, rows, cols, texts),
        frames=frames,
        interval=300,
        blit=True,
        repeat=False,
    )

    if save_path:
        animation.save(save_path, writer="pillow", fps=24)

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
