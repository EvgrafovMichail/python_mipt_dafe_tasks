from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def update_frame(
    frame_id: int,
    *,
    line: plt.Line2D,
    abscissa: np.ndarray,
    axis: plt.Axes,
    plot_duration: float,
    animation_step: float,
) -> tuple[plt.Line2D]:
    t = frame_id * animation_step
    axis.set_xlim(t, t + plot_duration)
    return (line,)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    total_duration = plot_duration + animation_step * num_frames
    abscissa = np.arange(0, total_duration, time_step)

    if modulation:
        envelope = modulation(abscissa)
    else:
        envelope = 1

    line = envelope * np.sin(2 * np.pi * fc * abscissa)

    max_amp = np.max(np.abs(line)) * 1.5
    if max_amp == 0:
        max_amp = 1.0

    figure, ax = plt.subplots(figsize=(16, 9))
    (line,) = ax.plot(abscissa, line, c="royalblue")
    ax.set_xlim(0, plot_duration)
    ax.set_ylim(-max_amp, max_amp)

    animation = FuncAnimation(
        figure,
        partial(
            update_frame,
            line=line,
            abscissa=abscissa,
            axis=ax,
            plot_duration=plot_duration,
            animation_step=animation_step,
        ),
        frames=num_frames,
        interval=50,
        blit=False,
    )

    if save_path:
        animation.save(save_path, writer="pillow", fps=20)

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
