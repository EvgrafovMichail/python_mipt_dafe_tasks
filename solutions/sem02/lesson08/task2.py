from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle


def create_mesh(maze: np.ndarray, axis: plt.Axes):
    hline_count, vline_count = maze.shape
    for i in range(hline_count):
        axis.axhline(i, color="black")
    for i in range(vline_count):
        axis.axvline(i, color="black")

def get_neighbors(maze: np.ndarray, current: tuple[int, int]):
    neighbors = []
    for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
        if 0 <= current[0] + x < maze.shape[0] \
            and 0 <= current[1] + y < maze.shape[1]\
            and maze[current[0] + x][current[1] + y] == 1:
            neighbors.append((current[0] + x, current[1] + y))
    return neighbors

def draw_circle(length: int, color: str,position: tuple[int, int], axis: plt.Axes):
    center_x = position[0] + 0.5
    center_y = position[1] + 0.5
    axis.add_patch(plt.Circle((center_x, center_y), 0.3, color=color))
    axis.text(center_x, center_y, str(length), color='white',
              ha='center', va='center', fontsize=12)

def count_steps(maze: np.ndarray, start: tuple[int, int], end: tuple[int, int]):
    count = 1
    queue = [start]
    visited = set(start)
    while queue:
        current = queue.pop(0)
        if current == end:
            return count
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        count += 1
    return count

def bfs(frame_number: int,
        *,
        queue: list[tuple[int, int]],
        distance: dict[tuple[int, int], int],
        maze: np.ndarray,
        end: tuple[int, int],
        axis: plt.Axes) -> plt.Axes:
    if queue:
        current = queue.pop(0)
        if current == end:
            draw_circle(distance[current], 'green', current, axis)
            return axis
        for neighbor in get_neighbors(maze, current):
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
        if distance[current] != 0:
            draw_circle(distance[current], 'red', current, axis)
        return axis
    return axis

def animate_wave_algorithm(
    maze: np.ndarray, 
    start: tuple[int, int], 
    end: tuple[int, int], 
    save_path: str = ""
)  -> FuncAnimation:
    figure, axis = plt.subplots()
    create_mesh(maze, axis)
    axis.set_title("Algorithm Li")
    for col in range(maze.shape[0]):
        for row in range(maze.shape[1]):
            if maze[col][row] == 0:
                axis.add_patch(Rectangle((col, row), 1, 1, facecolor='black', edgecolor='none'))

    queue = [start]
    distance = {start: 0}

    axis.set_xlim(0, maze.shape[0])
    axis.set_ylim(0, maze.shape[1])
    axis.set_aspect('equal')
    axis.grid(False)
    
    animation = FuncAnimation(
        fig=figure, 
        func=partial(bfs, maze=maze, queue=queue, distance=distance, end=end, axis=axis), 
        frames=count_steps(maze, start, end),
        interval=100,
    )
    if save_path != "":
        animation.save(save_path, writer="pillow", fps=10)
    return animation

if __name__ == "__main__":
    # Пример 1
    maze = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ])

    start = (2, 0)
    end = (5, 0)
    save_path = "labyrinth.gif"  # Укажите путь для сохранения анимации

    animation = animate_wave_algorithm(maze, start, end, save_path)
    HTML(animation.to_jshtml())
    
    # Пример 2
    
    maze_path = "./data/maze.npy"
    loaded_maze = np.load(maze_path)

    # можете поменять, если захотите запустить из других точек
    start = (6, 0)
    end = (5, 0)
    loaded_save_path = "loaded_labyrinth.gif"

    loaded_animation = animate_wave_algorithm(loaded_maze, start, end, loaded_save_path)
    HTML(loaded_animation.to_jshtml())
    
    