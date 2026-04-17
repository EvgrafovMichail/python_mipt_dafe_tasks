import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def animate_wave_algorithm(
    maze: np.ndarray, start: tuple[int, int], end: tuple[int, int], save_path: str = ""
) -> FuncAnimation:
    rows = maze.shape[0]
    cols = maze.shape[1]
    sr, sc = start
    er, ec = end
    dist = -np.ones_like(maze, dtype=int)
    dist[sr, sc] = 0
    current_front = [(sr, sc)]

    wave_frames = [dist.copy()]

    possible_move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    reached = False

    while current_front:
        next_front = []

        for r, c in current_front:
            if (r, c) == end:
                reached = True
                break

            for dr, dc in possible_move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if maze[nr, nc] == 1 and dist[nr, nc] == -1:
                        dist[nr, nc] = dist[r, c] + 1
                        next_front.append((nr, nc))
                        wave_frames.append(dist.copy())

        if reached:
            break
        current_front = next_front

    path_mask = np.zeros_like(maze, dtype=bool)
    if reached:
        r, c = end
        path_mask[r, c] = True
        d = dist[r, c]
        while (r, c) != (sr, sc):
            for dr, dc in possible_move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dist[nr, nc] == d - 1:
                        r, c = nr, nc
                        d -= 1
                        path_mask[r, c] = True
                        break

    def make_image(frame, show_path=False):
        h, w = frame.shape
        img = np.zeros((h, w, 3), dtype=float)
        img[:, :] = (1.0, 1.0, 1.0)
        walls = maze == 0
        img[walls] = (0.0, 0.0, 0.0)
        visited = frame >= 0
        img[visited] = (0.53, 0.81, 0.98)

        if show_path:
            path_and_visited = path_mask & (frame >= 0)
            img[path_and_visited] = (1.0, 0.8, 0.0)

        img[sr, sc] = (0.0, 1.0, 0.0)
        img[er, ec] = (1.0, 0.0, 0.0)

        return img

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xticks([])
    ax.set_yticks([])

    im = ax.imshow(make_image(wave_frames[0]), interpolation="nearest")

    texts = []

    total_wave_frames = len(wave_frames)
    extra_frames = 15
    total_frames = total_wave_frames + extra_frames

    def update(frame_id):
        ax.set_title("Волна")
        if frame_id < total_wave_frames:
            frame = wave_frames[frame_id]
            show_path = False
        else:
            frame = wave_frames[-1]
            show_path = reached

        im.set_data(make_image(frame, show_path=show_path))

        for r in range(rows):
            for c in range(cols):
                if frame[r, c] >= 0:
                    txt = ax.text(
                        c,
                        r,
                        str(frame[r, c]),
                        ha="center",
                        va="center",
                        fontsize=8,
                        color="black",
                    )
                    texts.append(txt)

        return (im, *texts)

    anim = FuncAnimation(
        fig,
        update,
        frames=total_frames,
        interval=500,
        blit=False,
    )

    if save_path:
        anim.save(save_path, writer="pillow")

    plt.close(fig)
    return anim


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
