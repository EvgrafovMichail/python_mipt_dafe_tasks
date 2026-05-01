from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def calculate_wave_propagation(maze, start, end):
    rows, cols = maze.shape
    dist = np.full((rows, cols), -1, dtype=int)
    dist[start] = 0

    history = [dist.copy()]
    found = False
    current_step = 0

    while not found:
        new = False
        for r in range(rows):
            for c in range(cols):
                if dist[r, c] == current_step:
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if maze[nr, nc] == 1 and dist[nr, nc] == -1:
                                dist[nr, nc] = current_step + 1
                                new = True
                                if (nr, nc) == end:
                                    found = True

        if not new:
            break

        current_step += 1
        history.append(dist.copy())

    return history, found


def update_frame(frame_idx, history, maze, img, ax):
    current_wave = history[frame_idx]
    display_data = np.where(maze == 0, -5, current_wave)
    img.set_data(display_data)
    ax.set_title(f"Распространение волны: шаг {frame_idx}")
    return [img]


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    history, found = calculate_wave_propagation(maze, start, end)

    if not found:
        print("Пути нет")

    fig, ax = plt.subplots(figsize=(6, 6))
    init_data = np.where(maze == 0, -5, -1)
    img = ax.imshow(init_data, cmap="viridis", animated=True, vmin=-5, vmax=len(history))
    ax.axis("off")

    ani = FuncAnimation(
        fig,
        partial(update_frame, history=history, maze=maze, img=img, ax=ax),
        frames=len(history),
        interval=200,
        blit=True,
        repeat=False,
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
