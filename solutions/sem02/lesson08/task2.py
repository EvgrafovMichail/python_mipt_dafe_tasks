from functools import partial
from queue import Queue

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class DrawMaze:
    def __init__(self, maze, start, finish, path):
        self.maze = maze
        self.start = start
        self.finish = finish
        self.save_path = path
        self._path = []
        self._colors = []
        self._shortest_path = []
        self._reachEndFlag = False
        self._msgCounter = 0
        self._possible_dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def _draw(self):
        figure, axis = plt.subplots(figsize=(16, 9))
        axis.imshow(self.maze, cmap="binary_r")
        return figure, axis

    def _findsolution(self):
        self._path = [list(self.start)]
        maze_wave = np.where(self.maze != 0, -1, -2)
        maze_wave[self.start[0], self.start[1]] = 0
        queue_frontier = Queue()
        queue_frontier.put(self.start)

        while not queue_frontier.empty():
            cur_elem = queue_frontier.get()
            if cur_elem[0] == self.finish[0] and cur_elem[1] == self.finish[1]:
                break
            cur_dist = maze_wave[cur_elem[0], cur_elem[1]]
            for dx, dy in self._possible_dir:
                temp = [cur_elem[0] + dx, cur_elem[1] + dy]
                if 0 <= temp[0] < maze_wave.shape[0] and 0 <= temp[1] < maze_wave.shape[1]:
                    if maze_wave[temp[0], temp[1]] == -1:
                        maze_wave[temp[0], temp[1]] = cur_dist + 1
                        self._path.append(temp)
                        queue_frontier.put(temp)

        self.maze_solution = maze_wave
        return

    def _backtrack(self):
        if self.maze_solution[self.finish[0], self.finish[1]] <= 0 and self.start != self.finish:
            print("There is no end")
            return
        cur = self.finish
        self._shortest_path.append(cur)
        print(self.start)
        while tuple(cur) != self.start:
            cur_dist = self.maze_solution[cur[0], cur[1]]
            for dx, dy in self._possible_dir:
                temp = [cur[0] + dx, cur[1] + dy]
                if (
                    0 <= temp[0] < self.maze_solution.shape[0]
                    and 0 <= temp[1] < self.maze_solution.shape[1]
                ):
                    if self.maze_solution[temp[0], temp[1]] == cur_dist - 1:
                        cur = temp
                        self._shortest_path.append(cur)
                        print(cur)

                        break
        return

    def update(self, frame, scate, axes, nums, visited):
        if frame == 0:
            visited.clear()
            self._colors = []
            self._reachEndFlag = False
            self._msgCounter = 0
            nums = []
        if frame < len(self._path):
            x, y = self._path[frame]
            search_msg = ["Searching.", "Searching..", "Searching..."]
            visited.append([y, x])
            if (x, y) == self.finish:
                self._reachEndFlag = True
                plt.title("This maze has a solution", loc="center", c="green")
                self._colors.append("green")

            else:
                if frame == len(self._path) - 1 and not self._reachEndFlag:
                    plt.title("No solution found", loc="center", c="red")
                elif not self._reachEndFlag:
                    plt.title(search_msg[self._msgCounter % 3], loc="center", c="blue")
                    self._msgCounter += 1
                self._colors.append("blue")

            if self.maze.size < 400:
                txt = axes.text(
                    y, x, self.maze_solution[x, y], color="red", ha="center", va="center"
                )
                nums.append(txt)
        else:
            backtrack_frame = frame - len(self._path)
            if backtrack_frame < len(self._shortest_path):
                x, y = self._shortest_path[backtrack_frame]
                target = [y, x]
                if target in visited:
                    idx = visited.index(target)
                    self._colors[idx] = "lime"

                if backtrack_frame == len(self._shortest_path) - 1:
                    plt.title("Shortest path highlighted!", loc="center", c="lime")

        scate.set_offsets(visited)
        scate.set_facecolors(self._colors)
        return [scate]

    def animate(self):
        self._findsolution()
        print(self.maze_solution)
        self._backtrack()
        print("Backtrack counted")
        figure, axis = self._draw()
        print(len(self._path))
        scat = axis.scatter([], [], s=100)
        nums = []
        visited = []
        total_frames = len(self._path) + len(self._shortest_path)
        print(self._shortest_path)
        animation = FuncAnimation(
            figure,
            partial(self.update, scate=scat, axes=axis, nums=nums, visited=visited),
            frames=range(total_frames),
            blit=True,
            interval=300,
            repeat=True,
        )
        if self.save_path != "":
            animation.save(self.save_path, writer="pillow", fps=30)
        return animation


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    maze = DrawMaze(maze, start, end, save_path)
    return maze.animate()


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

    maze_path = "C:\\MIPT_Progamming_studies\\Python_course\
                 \practice-homework\\solutions\\sem02\\lesson08\\data\\maze.npy"
    loaded_maze = np.load(maze_path).astype(np.int32)

    # можете поменять, если захотите запустить из других точек
    start = (2, 2)
    end = (99, 40)
    print(loaded_maze[2, 2])
    print(loaded_maze[99, 40])

    loaded_save_path = "loaded_labyrinth.gif"
    print(loaded_maze)
    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    # HTML(loaded_animation.to_jshtml())

    plt.show()
