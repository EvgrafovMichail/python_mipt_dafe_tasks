from collections import deque
from functools import partial
import queue

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def run_wave(maze: np.ndarray, start: tuple[int, int], end: tuple[int, int]):

    distances = np.full_like(maze, -1)
    distances[start] = 0

    vis_matrix = maze.astype(np.uint8)
    vis_matrix[start] = 2

    frames = [vis_matrix.copy()]
    queue = deque([start])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_x, max_y = maze.shape

    while queue:
        
        cells_at_current_level = len(queue)
        
        for j in range(cells_at_current_level):
            current_cell = queue.popleft()
            if current_cell == end:
                queue.clear() 
                break
                
            x, y = current_cell
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < max_x and 0 <= ny < max_y:
                    if maze[nx, ny] == 1 and distances[nx, ny] == -1:
                        distances[nx, ny] = distances[x, y] + 1
                        queue.append((nx, ny))
                        vis_matrix[nx, ny] = 2
                        
        frames.append(vis_matrix.copy())

    return distances, frames, vis_matrix


def restore_path(
    distances: np.ndarray, start: tuple[int, int], end: tuple[int, int], final_vis: np.ndarray
):

    frames = []

    if distances[end] == -1:
        return frames

    current_cell = end
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_x, max_y = distances.shape

    vis_matrix = final_vis.copy()

    while current_cell != start:
        vis_matrix[current_cell] = 3
        frames.append(vis_matrix.copy())

        x, y = current_cell
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < max_x and 0 <= ny < max_y and distances[nx, ny] == distances[x, y] - 1:
                vis_matrix[nx, ny] = 3
                current_cell = (nx, ny)
                break

    vis_matrix[start] = 3
    frames.append(vis_matrix.copy())

    return frames


def update(frame, frames, img):
    img.set_data(frames[frame])
    return [img]


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:

    distances, wave_frames, final_wave_vis = run_wave(maze, start, end)
    path_frames = restore_path(distances, start, end, final_wave_vis)

    all_frames = wave_frames + path_frames
    title = "Волновой алгоритм" if distances[end] != -1 else "Путь не найден!"

    fig = plt.figure()
    ax = plt.axes()
    fig.set_size_inches(8, 8)
    ax.set_title(title, fontsize=16)

    ax.set_xticks([])
    ax.set_yticks([])

    img = ax.imshow(all_frames[0], cmap = "viridis", vmin=0, vmax=3)

    animation = FuncAnimation(
        fig,
        partial(update, frames=all_frames, img=img),
        frames=len(all_frames),
        interval=200,
        blit=True,
    )

    if save_path:
        animation.save(save_path, writer="pillow", fps=10)

    return animation


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
    save_path = "labyrinth.gif"

    animation = animate_wave_algorithm(maze, start, end, save_path)
    HTML(animation.to_jshtml())

    maze_path = "./data/maze.npy"
    loaded_maze = np.load(maze_path)

    start = (2, 0)
    end = (5, 0)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
