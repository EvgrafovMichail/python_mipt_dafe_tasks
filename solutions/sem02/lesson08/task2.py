import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def animate_wave_algorithm(
    maze: np.ndarray,
    start: tuple[int, int],
    end: tuple[int, int],
    save_path: str = "",
) -> FuncAnimation:
    
    def solution_wave(maze, start, end):
        height, width = maze.shape
        distances = np.full(maze.shape, fill_value=-1, dtype=int)
        distances[start] = 0
        history = [distances.copy()]
        cur_wave = [start]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while cur_wave:
            next_wave = []
            for y, x in cur_wave:
                cur_value = distances[y, x]
                for move_y, move_x in moves:
                    new_y = y + move_y
                    new_x = x + move_x
                    if not (0 <= new_y < height and 0 <= new_x < width):
                        continue
                    if maze[new_y, new_x] != 1:
                        continue
                    if distances[new_y, new_x] != -1:
                        continue
                    distances[new_y, new_x] = cur_value + 1
                    next_wave.append((new_y, new_x))
            history.append(distances.copy())
            if distances[end] != -1:
                break
            cur_wave = next_wave
        return distances, history

    def path_recovery(distances, start, end):
        height, width = distances.shape
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        path = [end]
        cur_cell = end
        while cur_cell != start:
            cur_value = distances[cur_cell]
            for move_y, move_x in moves:
                new_y = cur_cell[0] + move_y
                new_x = cur_cell[1] + move_x
                if not (0 <= new_y < height and 0 <= new_x < width):
                    continue
                if distances[new_y, new_x] == cur_value - 1:
                    cur_cell = (new_y, new_x)
                    path.append(cur_cell)
                    break
        path.reverse()
        return path

    def build_frames(history, path, path_marker):
        frames = list(history)
        if path:
            state = history[-1].copy()
            for cell in path:
                state[cell] = path_marker
                frames.append(state.copy())
        return frames

    # алгос
    distances, history = solution_wave(maze, start, end)
    path_found = distances[end] != -1

    if path_found:
        path = path_recovery(distances, start, end)
    else:
        path = []
        print("Путь не найден")

    path_marker = distances.max() + 2 if path_found else 999
    frames = build_frames(history, path, path_marker)

    # графика
    figure, axis = plt.subplots(figsize=(8, 8))
    height, width = maze.shape

    axis.imshow(maze, cmap="gray", alpha=0.1)


    axis.set_xticks(np.arange(width + 1) - 0.5, minor=True)
    axis.set_yticks(np.arange(height + 1) - 0.5, minor=True)
    axis.grid(which="minor", color="black", linestyle="-", linewidth=0.5)
    axis.set_xticks([])
    axis.set_yticks([])

    texts = [
        [axis.text(x, y, "", ha="center", va="center") for x in range(width)] 
        for y in range(height)
    ]

    # обновление кадра
    def update(frame_id):
        curr_frame = frames[frame_id]
        for y in range(height):
            for x in range(width):
                val = curr_frame[y, x]
                if val == -1:
                    texts[y][x].set_text("")
                elif val == path_marker:
                    texts[y][x].set_text("*")
                    texts[y][x].set_color("red")
                else:
                    texts[y][x].set_text(str(val))
                    texts[y][x].set_color("black")
        return [t for row in texts for t in row]

    # анимация
    animation = FuncAnimation(
        figure,
        update,
        frames=len(frames),
        interval=200,
        blit=True,
    )

    if save_path:
        animation.save(save_path, writer="pillow", fps=5)

    return animation


if __name__ == "__main__":
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
    save_path = "labyrinth.gif"
    
    animation = animate_wave_algorithm(maze, start, end, save_path)
    HTML(animation.to_jshtml())