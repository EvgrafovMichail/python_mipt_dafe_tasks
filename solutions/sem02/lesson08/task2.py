import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap


def bfs(maze, start, end):
    rows, cols = maze.shape
    parents = {start: None}
    levels = [{start}]

    while levels[-1] and (end not in levels[-1]):
        next_level = set()
        for x, y in levels[-1]:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if (
                    (0 <= new_x < rows and 0 <= new_y < cols)
                    and (maze[new_x, new_y] != 0)
                    and ((new_x, new_y) not in parents)
                ):
                    parents[(new_x, new_y)] = (x, y)
                    next_level.add((new_x, new_y))
        if not next_level:
            break
        levels.append(next_level)

    path = []
    cur = end if end in parents else None
    while cur is not None:
        path.append(cur)
        cur = parents[cur]
    path.reverse()

    return levels, path


def animate_wave_algorithm(maze, start, end, save_path=""):
    rows, cols = maze.shape
    levels, path = bfs(maze, start, end)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(maze, cmap=ListedColormap(["hotpink", "lavenderblush"]))
    ax.set(xticks=[], yticks=[])
    ax.set_xticks(np.arange(-0.5, cols), minor=True)
    ax.set_yticks(np.arange(-0.5, rows), minor=True)
    ax.grid(which="minor", color="hotpink", linewidth=0.5)

    (dots,) = ax.plot(
        [], [], "o", color="white", markersize=22, markeredgecolor="hotpink", markeredgewidth=2
    )
    (line,) = ax.plot([], [], "-", color="hotpink", linewidth=5)

    def update(i):
        if i < len(levels):
            cells = levels[i]
            dots.set_data([c for r, c in cells], [r for r, c in cells])
            line.set_data([], [])
        else:
            dots.set_data([], [])
            line.set_data([c for r, c in path], [r for r, c in path])
        return dots, line

    anim = FuncAnimation(
        fig, update, frames=len(levels) + 15, interval=400, blit=False, repeat=False
    )
    if save_path:
        anim.save(save_path, writer="pillow", fps=3)
    return anim


if __name__ == "__main__":
    maze_small = np.array(
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

    animate_wave_algorithm(maze_small, start=(2, 0), end=(5, 0), save_path="labyrinth.gif")

    loaded_maze = np.load(
        "/Users/varvara/Developer/python_mipt_dafe_tasks/solutions/sem02/lesson08/data/maze.npy"
    )
    print("Размер загруженного лабиринта:", loaded_maze.shape)

    animate_wave_algorithm(
        loaded_maze, start=(18, 1), end=(37, 21), save_path="loaded_labyrinth.gif"
    )

    plt.show()
