from collections import deque
from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from matplotlib.colors import BoundaryNorm, ListedColormap

my_cmap = ListedColormap(["white", "black", "blue", "green"])
boundaries = [0, 0.5, 1.5, 3, 5]
norm = BoundaryNorm(boundaries, my_cmap.N)


class Wave_Animation:
    def __init__(
        self,
        maze: np.ndarray,
        axis: plt.Axes,
        start: tuple[int, int, int],
        end: tuple[int, int, int],
    ):
        self.maze = maze.copy()
        self.fontsize = 50 / max(maze.shape)
        self.way = np.zeros_like(maze, dtype=int)
        self.way[start[0], start[1]] = 1
        self.axis = axis
        self.img = axis.imshow(maze, cmap=my_cmap, norm=norm, origin="upper", zorder=1)
        self.start = start
        self.end = end
        self.queue = deque([start])
        self.text_grid = np.empty(maze.shape, dtype=object)
        for i in range(maze.shape[0]):
            for j in range(maze.shape[1]):
                self.text_grid[i, j] = self.axis.text(
                    j, i, "", ha="center", va="center", color="white", fontsize=8
                )

        t = self.text_grid[start[0], start[1]]
        t.set_text("0")
        t.set_color("white")
        t.set_fontsize(self.fontsize)

        axis.tick_params(axis="both", which="major", labelsize=self.fontsize)
        axis.set_xticks(range(maze.shape[1]))
        axis.set_yticks(range(maze.shape[0]))

        axis.set_xticks(np.arange(-0.5, maze.shape[1], 1), minor=True)
        axis.set_yticks(np.arange(-0.5, maze.shape[0], 1), minor=True)

        axis.grid(which="minor", color="black", linewidth=0.1, zorder=10)
        axis.grid(which="major", visible=False)

        if maze.shape[0] > 40:
            self.show_text = False
            self.axis.grid(False)
        else:
            self.show_text = True

    def __call__(self, frame_id: int):
        number = len(self.queue)

        if not self.queue:
            return None

        for _ in range(number):
            y, x, dist = self.queue.popleft()

            for neighbor in self._get_neighbors((y, x)):
                self.way[neighbor] = 1

                if self.show_text:
                    t = self.text_grid[neighbor]
                    t.set_text(str(dist + 1))
                    t.set_fontsize(self.fontsize)

                self.maze[neighbor] = 2

                if neighbor == self.end:
                    if self.show_text:
                        t.set_color("red")
                        t.set_fontsize(self.fontsize)
                    self.axis.set_title(f"Path found with length {dist + 1}")
                    self.maze[neighbor] = 4

                self.queue.append((*neighbor, dist + 1))

        self.img.set_data(self.maze)

        return [self.img]

    def _get_neighbors(self, coordinate: tuple[int, int]) -> list[tuple[int, int]]:
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_y, new_x = coordinate[0] + dx, coordinate[1] + dy
            if (
                0 <= new_x < self.maze.shape[1]
                and 0 <= new_y < self.maze.shape[0]
                and self.way[new_y, new_x] == 0
                and self.maze[new_y, new_x] == 1
            ):
                neighbors.append((new_y, new_x))
        return neighbors


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    figure, axis = plt.subplots(figsize=(8, 8))
    axis: plt.Axes

    axis.set_title("Wave Algorithm Animation")

    wave_animation = Wave_Animation(maze, axis, (*start, 0), end)

    animation = FuncAnimation(
        figure,
        partial(wave_animation),
        frames=1000,
        interval=50,
        repeat=False,
        blit=False,
    )

    plt.show()

    if save_path:
        animation.save(save_path, writer="pillow", fps=15, savefig_kwargs={"loop": 0})

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
    start = (2, 3)
    end = (70, 3)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
