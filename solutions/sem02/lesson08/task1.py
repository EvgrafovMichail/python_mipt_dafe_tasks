from functools import partial
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def update_frame(
    frame_id: int,
    *,
    modulation: Callable[[np.ndarray], np.ndarray] | None,
    fc: float,
    time_step: float,
    plot_duration: float,
    line: plt.Line2D,
    animation_step: float,
    axis: plt.Axes,
    limits: list[float],
) -> tuple[plt.Line2D]:
    time_start = frame_id * animation_step
    time_end = time_start + plot_duration

    abscissa = np.arange(time_start, time_end, time_step)
    ordinates = np.sin(2 * np.pi * fc * abscissa)
    if modulation is not None:
        ordinates *= modulation(abscissa)

    limits[0] = min(limits[0], ordinates.min())
    limits[1] = max(limits[1], ordinates.max())
    delta = limits[1] - limits[0] / 10

    line.set_data(abscissa, ordinates)
    axis.set_xlim(time_start, time_end)
    axis.set_ylim(limits[0] - delta, limits[1] + delta)

    return (line,)


def create_modulation_animation(
    modulation: Callable[[np.ndarray], np.ndarray] | None,
    fc: float,
    num_frames: int,
    plot_duration: float,
    time_step: float = 0.001,
    animation_step: float = 0.01,
    save_path: str = "",
) -> FuncAnimation:
    figure, axis = plt.subplots(figsize=(8, 8))
    (line,) = axis.plot([], [], c="aquamarine")

    limits = [np.inf, -np.inf]

    axis.set_xlabel("Время(с)")
    axis.set_ylabel("Амплитуда")
    axis.set_title("Анимация модулированного сигнала")

    update_function = partial(
        update_frame,
        modulation=modulation,
        fc=fc,
        time_step=time_step,
        plot_duration=plot_duration,
        line=line,
        animation_step=animation_step,
        axis=axis,
        limits=limits,
    )

    animation = FuncAnimation(
        figure,
        update_function,
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
