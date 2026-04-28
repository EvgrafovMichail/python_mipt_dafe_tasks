import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.style.use("default")


class Queue:
    def __init__(self, capacity: int) -> None:
        if capacity <= 1 or not isinstance(capacity, int):
            raise ValueError("The received capacity has an incorrect value")

        self.array = np.full(capacity, -1)
        self.size = 0
        self.capacity = capacity
        self.left = 0
        self.right = 0

    def __allocate(self) -> None:
        new_array = np.full(self.capacity * 2, -1)
        self.right = (self.right - 1 + self.capacity) % self.capacity

        if self.left > self.right:
            new_array[0 : self.capacity - self.left] = self.array[self.left : self.capacity]
            new_array[self.capacity - self.left : self.capacity] = self.array[0 : self.right + 1]
            self.left = 0
            self.right = self.capacity - 1
        else:
            new_array[0 : self.capacity] = self.array

        self.right = (self.right + 1) % self.capacity
        self.array = new_array
        self.capacity = self.capacity * 2

    def front(self) -> int:
        return self.array[self.left]

    def empty(self) -> bool:
        return self.size == 0

    def push(self, value: int) -> None:
        if self.size != 0 and self.right == self.left:
            self.__allocate()

        self.array[self.right] = value
        self.right = (self.right + 1) % self.capacity
        self.size += 1

    def pop(self) -> None:
        if self.left != self.right or (self.size != 0 and self.left == self.right):
            self.array[self.left] = -1
            self.left = (self.left + 1) % self.capacity
            self.size -= 1


def axes_init(maze: np.ndarray) -> tuple[plt.Figure, plt.Axes]:
    rows: int = maze.shape[0]
    columns: int = maze.shape[1]

    figure, axis = plt.subplots(figsize=(8, 8))
    axis.set_title(
        "BFS",
        fontsize=22,
        fontweight="bold",
        c="black",
        pad=25,
    )
    axis.set_xlim(0, columns)
    axis.set_ylim(0, rows)

    axis.imshow(
        maze,
        cmap="Greys",
        extent=[0, columns, 0, rows],
        origin="upper",
        interpolation="nearest",
        aspect="auto",
    )

    col_n = np.arange(columns + 1)
    row_n = np.arange(rows + 1)

    axis.set_xticks((col_n[:-1] + col_n[1:]) / 2)
    axis.set_yticks((row_n[:-1] + row_n[1:]) / 2)
    axis.set_xticklabels(np.arange(columns))
    axis.set_yticklabels(np.arange(rows - 1, -1, -1))
    axis.tick_params(
        axis="both",
        length=5,
        width=2,
        color="black",
    )

    axis1 = axis.twinx()
    axis2 = axis.twiny()

    axis1.set_yticks(row_n)
    axis2.set_xticks(col_n)
    axis1.set_yticklabels([])
    axis2.set_xticklabels([])
    axis1.tick_params(
        axis="y",
        length=0,
        width=2,
    )
    axis2.tick_params(
        axis="x",
        length=0,
        width=2,
    )

    axis1.grid(
        True,
        lw=2,
        color="black",
    )
    axis2.grid(
        True,
        lw=2,
        color="black",
    )

    return figure, axis


class FrameUpdater:
    def __init__(
        self,
        maze: np.ndarray,
        start: tuple[int, int],
        end: tuple[int, int],
        axis: plt.Axes,
        figure: plt.Figure,
    ) -> None:
        self.rows = maze.shape[0]
        self.columns = maze.shape[1]
        self.maze = maze
        self.end = end
        self.end_exist = False
        self.start_search = False

        self.axis = axis
        height_pts = axis.get_window_extent().height * 72 / figure.dpi
        self.fontsize = (height_pts / self.rows) * 0.4

        self.distance = np.full((self.rows, self.columns), -1)
        self.queue = Queue(self.columns)
        self.queue.push(start[0] * self.columns + start[1])
        self.distance[start[0], start[1]] = 0

    def __call__(
        self,
        frame_id: int,
    ) -> tuple[plt.Line2D]:
        if not self.start_search:
            while (
                self.distance[self.queue.front() // self.columns, self.queue.front() % self.columns]
                == frame_id
            ):
                x = self.queue.front() % self.columns
                y = self.queue.front() // self.columns
                self.queue.pop()

                if y == end[0] and x == end[1]:
                    self.end_exist = True
                color = "royalblue" if y != end[0] or x != end[1] else "green"
                self.axis.text(
                    x + 0.5,
                    self.rows - y - 0.5,
                    str(self.distance[y, x]),
                    va="center",
                    ha="center",
                    fontsize=self.fontsize,
                    color=color,
                    fontweight="bold",
                    zorder=10,
                )

                if (
                    x + 1 < self.columns
                    and self.maze[y, x + 1] == 1
                    and self.distance[y, x + 1] == -1
                ):
                    self.queue.push(y * self.columns + x + 1)
                    self.distance[y, x + 1] = self.distance[y, x] + 1

                if x - 1 >= 0 and self.maze[y, x - 1] == 1 and self.distance[y, x - 1] == -1:
                    self.queue.push(y * self.columns + x - 1)
                    self.distance[y, x - 1] = self.distance[y, x] + 1

                if y + 1 < self.rows and self.maze[y + 1, x] == 1 and self.distance[y + 1, x] == -1:
                    self.queue.push((y + 1) * self.columns + x)
                    self.distance[y + 1, x] = self.distance[y, x] + 1

                if y - 1 >= 0 and self.maze[y - 1, x] == 1 and self.distance[y - 1, x] == -1:
                    self.queue.push((y - 1) * self.columns + x)
                    self.distance[y - 1, x] = self.distance[y, x] + 1

        else:
            x = self.queue.front() % self.columns
            y = self.queue.front() // self.columns
            self.queue.pop()

            self.axis.text(
                x + 0.5,
                self.rows - y - 0.5,
                str(self.distance[y, x]),
                va="center",
                ha="center",
                fontsize=self.fontsize,
                color="red",
                fontweight="bold",
                zorder=10,
            )

            if (
                x + 1 < self.columns
                and self.maze[y, x + 1] == 1
                and self.distance[y, x + 1] < self.distance[y, x]
            ):
                self.queue.push(y * self.columns + x + 1)
            elif (
                x - 1 >= 0
                and self.maze[y, x - 1] == 1
                and self.distance[y, x - 1] < self.distance[y, x]
            ):
                self.queue.push(y * self.columns + x - 1)
            elif (
                y + 1 < self.rows
                and self.maze[y + 1, x] == 1
                and self.distance[y + 1, x] < self.distance[y, x]
            ):
                self.queue.push((y + 1) * self.columns + x)
            elif (
                y - 1 >= 0
                and self.maze[y - 1, x] == 1
                and self.distance[y - 1, x] < self.distance[y, x]
            ):
                self.queue.push((y - 1) * self.columns + x)

        return self.axis.get_lines()


class FrameGenerator:
    def __init__(self, updater: FrameUpdater) -> None:
        self.updater = updater

    def __call__(self):
        number = 0
        while not self.updater.queue.empty():
            yield number
            number += 1
        if self.updater.end_exist:
            self.updater.start_search = True
            self.updater.queue.push(
                self.updater.end[0] * self.updater.columns + self.updater.end[1]
            )
            while not self.updater.queue.empty():
                yield number
                number += 1
        else:
            print("The end was not found")


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    if maze[start[0], start[1]] == 0:
        raise ValueError("The start is in the wall")

    figure, axis = axes_init(maze)
    updater = FrameUpdater(maze, start, end, axis, figure)
    generator = FrameGenerator(updater)
    animation = FuncAnimation(
        figure,
        updater,
        frames=generator,
        interval=500,
        blit=True,
        save_count=10000,
    )
    if save_path != "":
        animation.save(
            save_path,
            writer="pillow",
            fps=3,
        )

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
    # HTML(animation.to_jshtml())

    # Пример 2
    """
    maze_path = "./data/maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (3, 3)
    end = (5, 0)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    # HTML(loaded_animation.to_jshtml())
    """
