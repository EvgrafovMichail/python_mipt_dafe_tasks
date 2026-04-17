from collections import deque

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation, PillowWriter


class WaveAnimator:
    def __init__(
        self, maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
    ):
        self.maze = maze
        self.start = start
        self.end = end
        self.save_path = save_path
        self.rows, self.cols = maze.shape
        self.step_height = 0.05
        self.found = False

        self.wave_frames, self.path = self._solve()

        visited_data = [(r, c, step) for step, wave in enumerate(self.wave_frames) for r, c in wave]
        self.visited = np.array(visited_data) if visited_data else np.empty((0, 3), dtype=int)
        self.path_arr = np.array(self.path) if self.path else np.empty((0, 2), dtype=int)

        self.fig = plt.figure(figsize=(10, 8))
        self.axis = self.fig.add_subplot(111, projection="3d")
        self._prepare_floor()

    def _solve(self) -> tuple[list[list[tuple[int, int]]], list[tuple[int, int]]]:
        distances, wave_frames = self._wave_steps()
        path = self._reconstruct_path(distances)
        return wave_frames, path

    def _wave_steps(self) -> tuple[np.ndarray, list[list[tuple[int, int]]]]:
        distances = np.full((self.rows, self.cols), -1)
        distances[self.start] = 0
        queue = deque([self.start])
        wave_frames = [[self.start]]
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while queue and not self.found:
            layer = [queue.popleft() for _ in range(len(queue))]
            next_wave = []

            for r, c in layer:
                if (r, c) == self.end:
                    self.found = True
                    break

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < self.rows
                        and 0 <= nc < self.cols
                        and self.maze[nr, nc] == 1
                        and distances[nr, nc] == -1
                    ):
                        distances[nr, nc] = distances[r, c] + 1
                        queue.append((nr, nc))
                        next_wave.append((nr, nc))

            if self.found:
                break
            if next_wave:
                wave_frames.append(next_wave)

        return distances, wave_frames

    def _reconstruct_path(self, distances: np.ndarray) -> list[tuple[int, int]]:
        path = []
        if self.found:
            curr = self.end
            path.append(curr)
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

            while curr != self.start:
                r, c = curr
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < self.rows
                        and 0 <= nc < self.cols
                        and distances[nr, nc] == distances[r, c] - 1
                    ):
                        curr = (nr, nc)
                        path.append(curr)
                        break
            path.reverse()

        return path

    def _prepare_floor(self):
        y_grid, x_grid = np.indices((self.rows, self.cols))

        self.floor_x = x_grid.flatten().astype(float)
        self.floor_y = y_grid.flatten().astype(float)
        self.floor_z = np.zeros_like(self.floor_x)

        self.floor_dx = np.ones_like(self.floor_x)
        self.floor_dy = np.ones_like(self.floor_x)
        self.floor_dz = np.full_like(self.floor_x, 0.01)

        self.floor_colors = np.where(
            self.maze.flatten()[:, None] == 0, [0.15, 0.15, 0.15, 1.0], [0.9, 0.9, 0.9, 1.0]
        )

    def _draw_frame(self, frame: int):
        self.axis.clear()

        len_waves = len(self.wave_frames)
        wave_phase = min(frame, len_waves - 1)
        path_phase = frame - len_waves

        if len(self.visited) > 0:
            active = self.visited[self.visited[:, 2] <= wave_phase]
            r, c, steps = active[:, 0], active[:, 1], active[:, 2]
            n_active = len(active)

            heights = (wave_phase - steps + 1) * self.step_height

            x_off = np.array([0.45, 0.35, 0.4])
            y_off = np.array([0.35, 0.45, 0.4])

            dx_vals = np.array([0.1, 0.3, 0.2])
            dy_vals = np.array([0.3, 0.1, 0.2])

            px = (c[:, None] + x_off).flatten()
            py = (r[:, None] + y_off).flatten()
            pz = np.full(3 * n_active, 0.01)

            pdx = np.tile(dx_vals, n_active)
            pdy = np.tile(dy_vals, n_active)
            pdz = np.repeat(heights, 3)

            if path_phase >= 0 and len(self.path_arr) > 0:
                active_path = self.path_arr[: path_phase + 1]
                idx = r * self.cols + c
                path_idx = active_path[:, 0] * self.cols + active_path[:, 1]
                is_path = np.isin(idx, path_idx)
            else:
                is_path = np.zeros(n_active, dtype=bool)

            base_colors = np.where(is_path[:, None], [0.9, 0.2, 0.2, 1.0], [0.2, 0.6, 0.9, 1.0])
            pc = np.repeat(base_colors, 3, axis=0)

            pos = tuple(
                np.concatenate([f, p])
                for f, p in zip((self.floor_x, self.floor_y, self.floor_z), (px, py, pz))
            )
            size = tuple(
                np.concatenate([f, p])
                for f, p in zip((self.floor_dx, self.floor_dy, self.floor_dz), (pdx, pdy, pdz))
            )
            colors = np.concatenate([self.floor_colors, pc])
        else:
            pos = (self.floor_x, self.floor_y, self.floor_z)
            size = (self.floor_dx, self.floor_dy, self.floor_dz)
            colors = self.floor_colors

        self.axis.bar3d(*pos, *size, color=colors, shade=True)

        self.axis.set_xlim(0, self.cols)
        self.axis.set_ylim(self.rows, 0)
        self.axis.set_zlim(0, max(self.rows, self.cols) * self.step_height + 0.5)

        self.axis.set_axis_off()

        self.axis.view_init(elev=70, azim=-45)

    def __call__(self) -> FuncAnimation:
        total_frames = len(self.wave_frames) + (len(self.path) if self.found else 0)

        anim = FuncAnimation(
            self.fig, self._draw_frame, frames=total_frames, interval=150, blit=False
        )

        if self.save_path:
            anim.save(self.save_path, writer=PillowWriter(fps=8))
        plt.close()
        return anim


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    return WaveAnimator(maze, start, end, save_path)()


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

    maze_path = "solutions/sem02/lesson08/data/maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (2, 0)
    end = (5, 0)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
