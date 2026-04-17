import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def create_modulation_animation(
    modulation,
    fc,
    num_frames,
    plot_duration,
    time_step=0.001,
    animation_step=0.01,
    save_path="",
) -> FuncAnimation:

    figure, axes = plt.subplots(figsize=(8, 6))

    t = np.arange(0, plot_duration, time_step)
    line, *_ = axes.plot([], [], color="blue")

    axes.set_xlim(0, plot_duration)
    axes.set_ylim(-1.5, 1.5)

    def update(frame):
        time_start = frame * animation_step
        time_end = t + time_start

        s = np.sin(2 * np.pi * fc * time_end)

        if modulation is None:
            y = s
        else:
            y = modulation(time_end) * s

        line.set_data(t, y)

        return (line,)

    animation = FuncAnimation(figure, update, frames=num_frames, interval=20, blit=True)

    if save_path != "":
        animation.save(save_path, writer="pillow", fps=24)

    return animation


if __name__ == "__main__":

    def modulation_function(t):
        return np.cos(t * 6)

    num_frames = 200
    plot_duration = np.pi / 2
    time_step = 0.001
    animation_step = 0.01
    fc = 50
    save_path_with_modulation = "modulated_signal.gif"

    animation = create_modulation_animation(
        modulation=modulation_function,
        fc=fc,
        num_frames=num_frames,
        plot_duration=plot_duration,
        time_step=time_step,
        animation_step=animation_step,
        save_path=save_path_with_modulation,
    )

    plt.show()
