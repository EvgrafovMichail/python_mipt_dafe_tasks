from functools import partial
from typing import Callable, Optional

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

plt.style.use("seaborn-v0_8")


def modulated_signal(t: np.ndarray, modulation: Optional[Callable], fc: float) -> np.ndarray:
    M = modulation if modulation is not None else lambda t: 1
    return M(t) * np.sin(2 * np.pi * fc * t)


def update_frame(frame_id: int, axis: plt.Axes, t_base: np.ndarray, step: float, signal: Callable):
    t_current = t_base + step * frame_id

    line = axis.get_lines()[0]
    line.set_xdata(t_current)
    line.set_ydata(signal(t_current))

    axis.set_xlim(t_current.min(), t_current.max())
    return axis.get_lines()


def setup_figure(plot_duration: float, time_step: float, signal: Callable):
    figure, axis = plt.subplots(figsize=(9, 6))
    t = np.linspace(0, plot_duration, int(plot_duration / time_step))
    axis.plot(t, signal(t), c="royalblue", label="Сигнал")
    axis.set_title("Анимация модулированного сигнала", fontsize=17, pad=20)
    axis.set_xlabel("Время (с)", fontsize=13, labelpad=7)
    axis.set_ylabel("Амплитуда", fontsize=13, labelpad=7)
    axis.set_ylim(-2, 2)
    plt.legend()
    return figure, axis, t


def create_modulation_animation(
    modulation: Optional[Callable],
    fc: float,
    num_frames: int,
    plot_duration: float,
    time_step: float = 0.001,
    animation_step: float = 0.01,
    save_path: str = "",
) -> FuncAnimation:
    signal = partial(modulated_signal, modulation=modulation, fc=fc)

    figure, axis, t_base = setup_figure(plot_duration, time_step, signal)

    animation = FuncAnimation(
        figure,
        lambda frame: update_frame(frame, axis, t_base, animation_step, signal),
        frames=num_frames,
        interval=1000 * animation_step,
        blit=True,
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
