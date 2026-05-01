from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def modulated_signal_math(modulation, fc, t):
    if modulation is None:
        return np.sin(2 * np.pi * fc * t)
    else:
        return modulation(t) * np.sin(2 * np.pi * fc * t)


def update(frame, modulation, fc, plot_duration, animation_step, time_step, line, ax):
    t_start = frame * animation_step
    t_end = t_start + plot_duration
    ax.set_xlim(t_start, t_end)
    t = np.linspace(t_start, t_end, int(plot_duration / time_step))
    signal = modulated_signal_math(modulation, fc, t)
    line.set_data(t, signal)
    return (line,)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes(xlim=(0, plot_duration))
    (line,) = ax.plot([], [], lw=2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("Время (с)", fontsize=14)
    ax.set_ylabel("Амплитуда", fontsize=14)
    fig.suptitle("Модулированный сигнал", fontsize=16)

    animation = FuncAnimation(
        fig,
        partial(
            update,
            modulation=modulation,
            fc=fc,
            plot_duration=plot_duration,
            animation_step=animation_step,
            time_step=time_step,
            line=line,
            ax=ax,
        ),
        frames=num_frames,
        interval=animation_step * 1000,
        blit=False,
    )

    if save_path:
        animation.save(save_path, writer="pillow", fps=30)

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
