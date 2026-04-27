from collections import deque

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    if maze[start] != 1:
        raise ValueError
    if maze[end] != 1:
        raise ValueError

    height, width = maze.shape

    wave_grid = np.full((height, width), -1, dtype=int)
    wave_grid[start] = 0

    queue = deque([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    wave_history = {0: [start]}

    while queue:
        current = queue.popleft()
        current_value = wave_grid[current]

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if not (0 <= nx < height and 0 <= ny < width):
                continue

            if maze[neighbor] == 1 and wave_grid[neighbor] == -1:
                wave_grid[neighbor] = current_value + 1
                queue.append(neighbor)

                if current_value + 1 not in wave_history:
                    wave_history[current_value + 1] = []
                wave_history[current_value + 1].append(neighbor)

                if neighbor == end:
                    queue.clear()
                    break

    wave_frames = []
    if np.any(wave_grid >= 0):
        max_wave = np.max(wave_grid[wave_grid >= 0])
        for step in range(int(max_wave) + 1):
            frame = np.full((height, width), -1, dtype=float)
            for i in range(step + 1):
                if i in wave_history:
                    for cell in wave_history[i]:
                        frame[cell] = i
            wave_frames.append(frame)

    path = None
    if wave_grid[end] != -1:
        path = [end]
        current = end
        while current != start:
            current_value = wave_grid[current]
            for dx, dy in directions:
                nx, ny = current[0] + dx, current[1] + dy
                neighbor = (nx, ny)
                if (
                    0 <= nx < height
                    and 0 <= ny < width
                    and wave_grid[neighbor] == current_value - 1
                ):
                    path.append(neighbor)
                    current = neighbor
                    break
        path.reverse()

    fig, ax = plt.subplots(figsize=(8, 8))

    maze_colors = np.zeros((height, width, 3))
    maze_colors[maze == 0] = [1.0, 1.0, 1.0]
    maze_colors[maze == 1] = [0.8, 0.8, 0.8]
    ax.imshow(maze_colors, interpolation="nearest")

    ax.set_xticks(np.arange(-0.5, width, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, height, 1), minor=True)
    ax.grid(True, which="minor", color="black", linestyle="-", linewidth=1)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])

    ax.scatter(start[1], start[0], color="green", s=200, marker="s", label="Start", zorder=5)
    ax.scatter(end[1], end[0], color="red", s=200, marker="s", label="End", zorder=5)
    ax.legend(loc="upper right")

    def init():
        return []

    def update(frame_idx):
        for artist in ax.images[1:]:
            artist.remove()
        for artist in ax.texts[:]:
            artist.remove()

        current_frame = wave_frames[frame_idx]

        wave_overlay = np.zeros((height, width, 4))
        mask = current_frame >= 0

        if np.any(mask):
            wave_overlay[mask, 0] = 0.79
            wave_overlay[mask, 1] = 0.62
            wave_overlay[mask, 2] = 0.34
            wave_overlay[mask, 3] = 0.5

        ax.imshow(wave_overlay, interpolation="nearest")

        for i in range(height):
            for j in range(width):
                if current_frame[i, j] >= 0:
                    ax.text(
                        j,
                        i,
                        str(int(current_frame[i, j])),
                        ha="center",
                        va="center",
                        color="black",
                        fontsize=12,
                        fontweight="bold",
                    )

        if frame_idx == len(wave_frames) - 1 and path:
            path_y, path_x = zip(*path)
            ax.plot(path_x, path_y, "g-", linewidth=3, zorder=4)

        return []

    anim = FuncAnimation(
        fig, update, init_func=init, frames=len(wave_frames), interval=500, blit=False, repeat=True
    )

    if save_path:
        try:
            if not save_path.endswith(".gif"):
                save_path += ".gif"
            anim.save(save_path, writer="pillow", fps=2)
            print(f"Анимация сохранена в {save_path}")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")

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
    save_path = "./solutions/sem02/lesson08/gifs/labyrinth.gif"
    # Укажите путь для сохранения анимации

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
