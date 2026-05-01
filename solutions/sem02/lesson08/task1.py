from functools import partial
from typing import Callable, Tuple

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes


def calculate_plot_limits(
    frame: int, animation_step: float, plot_duration: float
) -> Tuple[float, float]:
    left_time = frame * animation_step
    return left_time, left_time + plot_duration


def calculate_modulated_func(
    modulation: Callable[[np.ndarray], np.ndarray], fc: float
) -> Callable[[np.ndarray], np.ndarray]:
    if modulation is None:
        lambda t: np.sin(2 * np.pi * fc * t)

    return lambda t: np.sin(2 * np.pi * fc * t) * modulation(t)


def calculate_signal_points(
    time_range: Tuple[float, float], num_points: int, func: Callable[[float], np.ndarray]
) -> Tuple[np.ndarray, np.ndarray]:
    time = np.linspace(*time_range, num_points)
    abscissa = time
    ordinate = func(time)

    return abscissa, ordinate


def update_axis(
    axis: Axes, time_range: Tuple[float, float], abscissa: np.ndarray, ordinate: np.ndarray
) -> None:
    line, *_ = axis.lines
    axis.set_xlim(*time_range)
    line.set_xdata(abscissa)
    line.set_ydata(ordinate)


def update_frame(
    frame: int,
    animation_step: float,
    num_points: int,
    plot_duration: float,
    axis: Axes,
    func: Callable[[float], np.ndarray],
) -> None:
    time_range = calculate_plot_limits(frame, animation_step, plot_duration)
    abscissa, ordinate = calculate_signal_points(time_range, num_points, func)

    update_axis(axis, time_range, abscissa, ordinate)


def style_axis(axis: Axes):
    axis.set_title("Анимация модулированного сигнала")
    axis.set_ylabel("Амплитуда")
    axis.set_xlabel("Время (с)")
    axis.lines[0].set_label("сигнал")
    axis.legend(loc="upper right")


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    num_points = int(plot_duration / time_step)
    figure, axis = plt.subplots(figsize=(8, 5))
    time_range = calculate_plot_limits(0, animation_step, plot_duration)
    signal_func = calculate_modulated_func(modulation, fc)

    axis.plot(*calculate_signal_points(time_range, num_points, signal_func))
    style_axis(axis)

    animation = FuncAnimation(
        figure,
        partial(
            update_frame,
            animation_step=animation_step,
            plot_duration=plot_duration,
            axis=axis,
            func=signal_func,
            num_points=num_points,
        ),
        frames=num_frames,
        interval=animation_step * 1000,
    )

    if save_path:
        animation.save(save_path)

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
