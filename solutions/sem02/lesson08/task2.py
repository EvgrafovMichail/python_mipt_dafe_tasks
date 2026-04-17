from collections import deque
from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap


def _run_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int]
) -> tuple[list[tuple[int, int, int]], list[tuple[int, int]]]:
    rows, cols = maze.shape
    distances = np.full((rows, cols), -1, dtype=int)
    distances[start] = 0

    queue = deque([start])

    wave_steps = [(start[0], start[1], 0)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    found = False

    while queue:
        curr_r, curr_c = queue.popleft()

        if (curr_r, curr_c) == end:
            found = True
            break

        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr, nc] == 1 and distances[nr, nc] == -1:
                    distances[nr, nc] = distances[curr_r, curr_c] + 1
                    queue.append((nr, nc))
                    wave_steps.append((nr, nc, distances[nr, nc]))

    path_steps = []
    if found:
        curr = end
        path_steps.append(curr)
        while curr != start:
            for dr, dc in directions:
                nr, nc = curr[0] + dr, curr[1] + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if distances[nr, nc] == distances[curr] - 1:
                        curr = (nr, nc)
                        path_steps.append(curr)
                        break
        path_steps.reverse()

    return wave_steps, path_steps


def _update_animation(
    frame: int,
    wave_artists: list[dict],
    path_line,
    wave_steps: list[tuple[int, int, int]],
    path_steps: list[tuple[int, int]],
):
    if frame < len(wave_steps):
        r, c, dist = wave_steps[frame]
        artist = wave_artists[frame]

        artist["circle"].set_data([c], [r])
        artist["text"].set_position((c, r))
        artist["text"].set_text(str(dist))
        artist["text"].set_visible(True)

    elif frame == len(wave_steps) and path_steps:
        path_r = [p[0] for p in path_steps]
        path_c = [p[1] for p in path_steps]
        path_line.set_data(path_c, path_r)

    return []


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    if maze[start] == 0 or maze[end] == 0:
        print("Ошибка: Старт или Финиш находятся в стене (0).")
        wave_steps, path_steps = [], []
    else:
        wave_steps, path_steps = _run_wave_algorithm(maze, start, end)
    COLOR_WALL = "#2D3142"  # Темно-сине-серый
    COLOR_PATH = "#E0E4E8"  # Светлый серо-голубой
    COLOR_GRID = "#1C1F2B"  # Темная сетка для контраста
    COLOR_WAVE_BG = "#FF0054"  # Яркий малиновый для кружка
    COLOR_WAVE_FG = "#FFFFFF"  # Белый текст цифр
    COLOR_RESULT = "#00F5D4"  # Неоновый бирюзовый для пути

    custom_cmap = ListedColormap([COLOR_WALL, COLOR_PATH])

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.imshow(maze, cmap=custom_cmap, vmin=0, vmax=1)

    rows, cols = maze.shape
    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which="minor", color=COLOR_GRID, linestyle="-", linewidth=2.5)
    ax.tick_params(which="minor", size=0)

    ax.set_xticks(np.arange(0, cols, 1))
    ax.set_yticks(np.arange(0, rows, 1))

    fig.patch.set_facecolor("#F8F9FA")
    ax.set_title("Волновой алгоритм", pad=15, fontsize=15, fontweight="bold", color="#2D3142")

    wave_artists = []
    for _ in range(len(wave_steps)):
        (circle,) = ax.plot(
            [], [], marker="o", color=COLOR_WAVE_BG, markersize=19, linestyle="None", zorder=3
        )
        txt = ax.text(
            0,
            0,
            "",
            color=COLOR_WAVE_FG,
            ha="center",
            va="center",
            fontweight="bold",
            fontsize=11,
            zorder=4,
            visible=False,
        )
        wave_artists.append({"circle": circle, "text": txt})

    (path_line,) = ax.plot(
        [],
        [],
        color=COLOR_RESULT,
        linewidth=5,
        alpha=0.9,
        solid_capstyle="round",
        solid_joinstyle="round",
        zorder=5,
    )

    total_frames = len(wave_steps) + 1 if wave_steps else 1

    update_func = partial(
        _update_animation,
        wave_artists=wave_artists,
        path_line=path_line,
        wave_steps=wave_steps,
        path_steps=path_steps,
    )

    ani = FuncAnimation(
        fig, update_func, frames=total_frames, blit=False, interval=250, repeat=False
    )

    if save_path:
        ani.save(save_path, writer="pillow")

    plt.close(fig)
    return ani


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
