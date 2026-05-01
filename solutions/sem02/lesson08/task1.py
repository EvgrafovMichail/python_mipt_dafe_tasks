from functools import partial
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def calculate_signal(
    modulation: Callable | None,
    fc: int,
    num_frames: int,
    plot_duration: float,
    animation_step: float = 0.01,
) -> tuple[np.ndarray, np.ndarray]:
    if modulation is None:

        def base_modulation(t: float) -> float:
            return 1.0

        modulation = base_modulation
    total_time = num_frames * animation_step + plot_duration
    t = np.arange(0, total_time, time_step)
    s = modulation(t) * np.sin(2 * np.pi * fc * t)
    return t, s


def create_modulation_animation(
    modulation: Callable | None,
    fc: int,
    num_frames: int,
    plot_duration: float,
    time_step: float = 0.001,
    animation_step: float = 0.01,
    save_path: str = "",
) -> FuncAnimation:
    if fc < 0:
        raise ValueError("Frequency must not be negative")
    if num_frames <= 0:
        raise ValueError("Numbers of frames must ne positive")
    if plot_duration <= 0:
        raise ValueError("Plot duration must ne positive")
    if time_step <= 0:
        raise ValueError("Time step must ne positive")
    if animation_step <= 0:
        raise ValueError("Animation step must ne positive")

    plt.style.use("ggplot")

    t, s = calculate_signal(
        modulation=modulation,
        fc=fc,
        num_frames=num_frames,
        plot_duration=plot_duration,
        animation_step=animation_step,
    )

    abscissa = np.arange(0, plot_duration, time_step)

    figure, axis = plt.subplots()
    axis.set_xlabel("Время (с)")
    axis.set_ylabel("Амплитуда")
    axis.set_title("Анимация модулированного сигнала")

    axis.set_xlim(0, plot_duration)
    axis.set_ylim(1.5 * s.min(), 1.5 * s.max())

    line, *_ = axis.plot(
        abscissa,
        np.sin(abscissa),
        c="royalblue",
        label="Модулированный сигнал",
    )
    axis.legend(loc="upper right")

    def update_frame(
        frame_id: int,
        *,
        line: plt.Line2D,
        plot_duration: float,
        animation_step: float,
    ) -> tuple[plt.Line2D]:
        t_start = frame_id * animation_step
        t_end = t_start + plot_duration
        mask = (t >= t_start) & (t <= t_end)
        t_curr = t[mask]
        s_curr = s[mask]
        line.set_data(t_curr, s_curr)
        axis.set_xlim(t_start, t_end)
        return (line,)

    animation = FuncAnimation(
        figure,
        partial(
            update_frame,
            line=line,
            plot_duration=plot_duration,
            animation_step=animation_step,
        ),
        frames=num_frames,
        interval=animation_step,
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
