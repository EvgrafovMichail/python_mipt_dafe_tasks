from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    def wave(maze, start, end):
        x, y = maze.shape
        wave = np.ones(shape=maze.shape, dtype=int) * (-1)
        wave[start] = 0
        free_mask = maze == 1
        history = [wave.copy()]
        step = 0
        found = False

        while not found:
            mask = wave == step

            if not mask.any():
                break

            up = np.zeros(shape=mask.shape, dtype=bool)
            down = np.zeros(shape=mask.shape, dtype=bool)
            left = np.zeros(shape=mask.shape, dtype=bool)
            right = np.zeros(shape=mask.shape, dtype=bool)

            up[:-1, :] = mask[1:, :]
            down[1:, :] = mask[:-1, :]
            left[:, :-1] = mask[:, 1:]
            right[:, 1:] = mask[:, :-1]

            near = up | down | left | right
            can_go_next = near & free_mask & (wave == -1)

            if not can_go_next.any():
                break

            wave[can_go_next] = step + 1

            if wave[end] != -1:
                found = True

            step += 1
            history.append(wave.copy())

        path = []
        if found:
            curr = end
            path.append(curr)
            while curr != start:
                for nowi, nowj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    previ, prevj = curr[0] + nowi, curr[1] + nowj
                    if 0 <= previ < x and 0 <= prevj < y:
                        if wave[previ, prevj] == wave[curr] - 1:
                            curr = (previ, prevj)
                            path.append(curr)
                            break

        return history, path, found

    def update_frame(frame_id, axis, maze, history, path, found, h, w):
        axis.clear()

        data = history[min(frame_id, len(history) - 1)]

        for i in range(h):
            for j in range(w):
                if maze[i, j] == 0:
                    color = "white"
                else:
                    if data[i, j] >= 0:
                        color = "lightpink"
                    else:
                        color = "black"
                axis.add_patch(
                    plt.Rectangle((j, h - 1 - i), 1, 1, facecolor=color, edgecolor="black")
                )

        for i in range(h):
            for j in range(w):
                if data[i, j] >= 0 and maze[i, j] == 1:
                    axis.text(
                        j + 0.5,
                        h - 1 - i + 0.5,
                        str(data[i, j]),
                        ha="center",
                        va="center",
                        fontsize=8,
                    )

        axis.scatter(start[1] + 0.5, h - 1 - start[0] + 0.5, c="red", s=100)
        axis.scatter(end[1] + 0.5, h - 1 - end[0] + 0.5, c="olivedrab", s=100)

        if frame_id == len(history) - 1 and found:
            for i, j in path:
                axis.add_patch(
                    plt.Rectangle((j, h - 1 - i), 1, 1, facecolor="lightgreen", edgecolor="black")
                )

        axis.set_xlim(0, w)
        axis.set_ylim(0, h)

        return

    h, w = maze.shape
    history, path, found = wave(maze, start, end)

    figure, axis = plt.subplots(figsize=(8, 8))

    animation = FuncAnimation(
        figure,
        partial(
            update_frame, axis=axis, maze=maze, history=history, path=path, found=found, h=h, w=w
        ),
        frames=len(history),
        interval=200,
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
    plt.show()

    # Пример 2
    """
    ##maze_path = "./data/maze.npy"
    maze_path = "D:/GitHub/python_mipt_dafe_tasks/solutions/sem02/lesson08/data/maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (2, 0)
    end = (5, 0)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
    """
