from functools import partial
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def get_signal(
    time: np.ndarray,
    modulation: Callable[[np.ndarray], np.ndarray] | None,
    fc: float,
) -> np.ndarray:
    carrier = np.sin(2 * np.pi * fc * time)
    if modulation is None:
        return carrier
    return modulation(time) * carrier


def get_signal_limits(
    modulation: Callable[[np.ndarray], np.ndarray] | None,
    fc: float,
    num_frames: int,
    plot_duration: float,
    time_step: float,
    animation_step: float,
) -> tuple[float, float]:
    max_time = plot_duration + animation_step * max(num_frames - 1, 0)
    time = np.arange(0, max_time + time_step, time_step)
    signal = get_signal(time, modulation, fc)
    max_abs_value = np.max(np.abs(signal))

    if max_abs_value == 0:
        max_abs_value = 1.0

    limit = max_abs_value * 2.01
    return -limit, limit


def create_modulation_animation(
    modulation,
    fc,
    num_frames,
    plot_duration,
    time_step=0.001,
    animation_step=0.01,
    save_path="",
) -> FuncAnimation:
    start_time = 0
    time = np.arange(start_time, start_time + plot_duration, time_step)
    signal = get_signal(time, modulation, fc)

    plt.style.use("ggplot")
    figure, axis = plt.subplots(figsize=(12, 6))
    (line,) = axis.plot(time, signal, c="royalblue", label="signal")

    axis.set_title(
        "Анимация модулированного сигнала",
        fontsize=16,
        fontweight="bold",
        c="dimgray",
    )
    axis.set_xlabel("Время (с)", fontsize=12, fontweight="bold", c="dimgray")
    axis.set_ylabel("Амплитуда", fontsize=12, fontweight="bold", c="dimgray")
    axis.set_xlim(time.min(), time.max())
    axis.set_ylim(
        *get_signal_limits(
            modulation,
            fc,
            num_frames,
            plot_duration,
            time_step,
            animation_step,
        )
    )
    axis.legend()

    def update_frame(
        frame_id: int,
        *,
        line: plt.Line2D,
        axis: plt.Axes,
        modulation: Callable[[np.ndarray], np.ndarray] | None,
        fc: float,
        plot_duration: float,
        time_step: float,
        animation_step: float,
    ) -> tuple[plt.Line2D]:
        frame_start = frame_id * animation_step
        frame_time = np.arange(
            frame_start,
            frame_start + plot_duration,
            time_step,
        )
        frame_signal = get_signal(frame_time, modulation, fc)

        line.set_data(frame_time, frame_signal)
        axis.set_xlim(frame_time.min(), frame_time.max())
        return (line,)

    animation = FuncAnimation(
        figure,
        partial(
            update_frame,
            line=line,
            axis=axis,
            modulation=modulation,
            fc=fc,
            plot_duration=plot_duration,
            time_step=time_step,
            animation_step=animation_step,
        ),
        frames=num_frames,
        interval=50,
        blit=True,
    )

    if save_path != "":
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
