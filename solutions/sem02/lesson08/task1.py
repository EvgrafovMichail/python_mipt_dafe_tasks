from functools import partial

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def signal(abscissa, fc, modulation):
    if modulation:
        m_t = modulation(abscissa)
    else:
        m_t = 1.0
    return m_t * np.sin(2 * np.pi * fc * abscissa)


def update(num_frame, line, fc, modulation, plot_duration, time_step, animation_step):

    t_start = num_frame * animation_step
    t_end = t_start + plot_duration

    abscissa = np.arange(t_start, t_end, time_step)
    ordinates = signal(abscissa, fc, modulation)

    line.set_xdata(abscissa - t_start)
    line.set_ydata(ordinates)
    return [line]


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:

    figure, axis = plt.subplots(figsize=(16, 9))
    axis: plt.Axes

    abscissa = np.arange(0, plot_duration, time_step)
    ordinates = signal(abscissa, fc, modulation=modulation)

    axis.set_ylim(ordinates.min() * 1.25, ordinates.max() * 1.25)
    axis.set_xlim(0, plot_duration)

    line, *_ = axis.plot(
        abscissa,
        ordinates,
        c="red",
        label="Сигнал",
    )

    axis.set_xlabel("Время (с)", fontsize=14)
    axis.set_ylabel("Амплитуда", fontsize=14)
    axis.set_title("Визуализация модулированного сигнала", fontsize=20, fontweight="bold")

    axis.legend(fontsize=12)

    animation = FuncAnimation(
        figure,
        partial(
            update,
            line=line,
            fc=fc,
            modulation=modulation,
            plot_duration=plot_duration,
            time_step=time_step,
            animation_step=animation_step,
        ),
        num_frames,
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
