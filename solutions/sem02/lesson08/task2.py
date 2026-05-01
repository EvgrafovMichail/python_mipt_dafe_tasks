import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def run(maze, start, end):
    rows, cols = maze.shape
    wave = np.full((rows, cols), -1)
    wave[start] = 0

    queue = [start]
    frames = [wave.copy()]

    while queue:
        r, c = queue.pop(0)

        if (r, c) == end:
            break

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and maze[nr, nc] == 1 and wave[nr, nc] == -1:
                wave[nr, nc] = wave[r, c] + 1
                queue.append((nr, nc))

        frames.append(wave.copy())

    return wave, frames


def find_path(wave, start, end):
    if wave[end] == -1:
        return set()

    path = {end}
    r, c = end
    while (r, c) != start:
        found = False
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < wave.shape[0] and 0 <= nc < wave.shape[1]:
                if wave[nr, nc] == wave[r, c] - 1:
                    path.add((nr, nc))
                    r, c = nr, nc
                    found = True
                    break
        if not found:
            break

    return path


def make_frame(maze, wave, path=None):
    grid = maze.copy()

    grid[wave >= 0] = 2

    if path:
        for r, c in path:
            grid[r, c] = 3

    return grid


def animate_wave_algorithm(maze, start, end, save_path=""):
    wave, frames = run(maze, start, end)

    path = find_path(wave, start, end)

    if not path:
        print("Путь не найден.")

    figure, axis = plt.subplots(figsize=(6, 6))
    frame = axis.imshow(make_frame(maze, frames[0]), cmap="cool", vmin=0, vmax=3)
    axis.grid(False)

    all_frames = [make_frame(maze, f) for f in frames]
    all_frames.append(make_frame(maze, frames[-1], path))

    def update_frame(frame_id: int) -> tuple[plt.AxesImage]:
        frame.set_data(all_frames[frame_id])
        return (frame,)

    animation = FuncAnimation(
        figure,
        update_frame,
        frames=len(all_frames),
        interval=100,
        blit=True,
    )

    animation.save(save_path, writer="pillow", fps=24)

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
    start = (2, 0)
    end = (5, 0)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
