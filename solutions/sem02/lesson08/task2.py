from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap  # !!!


# Пусть путь всегда существует
def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    starting_maze = maze.copy()

    def make_visual(p_ways):
        visual = np.where(starting_maze == 0, 0, 1)
        visual[p_ways >= 0] = 2
        return visual

    p_ways = np.full_like(maze, -1)
    coordinates = [start]
    steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    head = 0
    p_ways[start] = 0

    frames = [make_visual(p_ways)]
    current_dist = 0

    while head < len(coordinates):
        dist = p_ways[coordinates[head]]
        if dist > current_dist:
            frames.append(make_visual(p_ways))
            current_dist = dist

        maze[coordinates[head]] = 7
        for i in range(len(steps)):
            shift_up_down = coordinates[head][0] + steps[i][0]
            shift_left_right = coordinates[head][1] + steps[i][1]
            if ((0 <= shift_left_right < maze.shape[1]) == False) or (
                (0 <= shift_up_down < maze.shape[0]) == False
            ):
                continue
            if maze[shift_up_down, shift_left_right] == 1:
                coordinates.append((shift_up_down, shift_left_right))
                p_ways[shift_up_down, shift_left_right] = p_ways[coordinates[head]] + 1
        head += 1

    figure, axes = plt.subplots(figsize=(12, 12))
    cmap = ListedColormap(["green", "brown", "blue"])
    image = axes.imshow(
        frames[0],
        cmap=cmap,
    )
    axes.set_xticks(np.arange(starting_maze.shape[1]))
    axes.set_yticks(np.arange(starting_maze.shape[0]))
    axes.set_xticklabels(np.arange(starting_maze.shape[1]))
    axes.set_yticklabels(np.arange(starting_maze.shape[0]))

    axes.set_xticks(np.arange(-0.5, starting_maze.shape[1], 1), minor=True)
    axes.set_yticks(np.arange(-0.5, starting_maze.shape[0], 1), minor=True)

    axes.grid(which="minor", color="black", linestyle="-", linewidth=2)
    axes.grid(which="major", visible=False)

    axes.set_title("Волновой алгоритм", fontsize=16)

    def update(frame_id):
        image.set_data(frames[frame_id])
        return [image]

    anim = FuncAnimation(figure, update, frames=len(frames), interval=100, blit=True, repeat=False)

    if save_path:
        anim.save(save_path, writer="pillow")

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
    save_path = "labyrinth.gif"  # Укажите путь для сохранения анимации

    animation = animate_wave_algorithm(maze, start, end, save_path)
    HTML(animation.to_jshtml())

    """ maze_path = "./data/maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (2, 0)
    end = (5, 0)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml()) """
