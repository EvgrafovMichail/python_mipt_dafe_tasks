from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def compute_signal(time: np.ndarray, modulation, fc: float) -> np.ndarray:
    carrier = np.sin(2 * np.pi * fc * time)
    if modulation is None:
        return carrier
    return modulation(time) * carrier


def update_frame(
    frame_id: int,
    *,
    line: plt.Line2D,
    signal: np.ndarray,
    window_size: int,
    step_size: int,
) -> tuple[plt.Line2D]:
    start = frame_id * step_size
    line.set_ydata(signal[start : start + window_size])
    return (line,)


def create_modulation_animation(
    modulation,
    fc,
    num_frames,
    plot_duration,
    time_step=0.001,
    animation_step=0.01,
    save_path="",
) -> FuncAnimation:
    total_duration = (num_frames - 1) * animation_step + plot_duration
    time = np.linspace(0, total_duration, int(total_duration / time_step))
    signal = compute_signal(time, modulation, fc)

    window_size = int(plot_duration / time_step)
    step_size = int(animation_step / time_step)

    figure, axis = plt.subplots(figsize=(16, 9))
    axis.set_xlim(time[0], time[window_size - 1])
    axis.set_ylim(signal.min() - 0.1, signal.max() + 0.1)

    line, *_ = axis.plot(time[:window_size], signal[:window_size], c="royalblue")

    animation = FuncAnimation(
        figure,
        partial(
            update_frame, line=line, signal=signal, window_size=window_size, step_size=step_size
        ),
        frames=num_frames,
        interval=50,
        blit=True,
    )

    if save_path:
        animation.save(save_path, writer="pillow", fps=24)

    return animation


if __name__ == "__main__":

    def modulation_function(t):
        return np.cos(t * 6)

    num_frames = 100
    plot_duration = np.pi / 2
    time_step = 0.001
    animation_step = np.pi / 200
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
    HTML(animation.to_jshtml())
