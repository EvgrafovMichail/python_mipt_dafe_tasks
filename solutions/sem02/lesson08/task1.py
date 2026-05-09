from functools import partial

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from traitlets import Callable


def get_modulated_signal(t: np.ndarray, modulation: Callable, fc: float) -> np.ndarray:
    m_t = modulation(t) if modulation is not None else 1.0
    return m_t * np.sin(2 * np.pi * fc * t)


def update_frame(
    frame_id: int,
    *,
    line: plt.Line2D,
    axis: plt.Axes,
    base_abscissa: np.ndarray,
    modulation: Callable,
    fc: float,
    plot_duration: float,
    animation_step: float,
) -> tuple[plt.Line2D]:
    shift = frame_id * animation_step

    current_t = base_abscissa + shift

    ordinates = get_modulated_signal(current_t, modulation, fc)

    line.set_data(current_t, ordinates)

    axis.set_xlim(shift, shift + plot_duration)

    return (line,)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    num_points = int(plot_duration / time_step)
    base_abscissa = np.linspace(0, plot_duration, num_points)

    figure, axis = plt.subplots(figsize=(12, 6))

    axis.set_ylabel("Амплитуда")
    axis.set_xlabel("Время (с)")
    axis.set_ylim(-2.0, 2.0)

    (line,) = axis.plot([], [], c="royalblue", label="Сигнал")

    axis.legend()

    # Привязываем функцию обновления
    anim_func = partial(
        update_frame,
        line=line,
        axis=axis,
        base_abscissa=base_abscissa,
        modulation=modulation,
        fc=fc,
        plot_duration=plot_duration,
        animation_step=animation_step,
    )

    anim = FuncAnimation(figure, anim_func, frames=num_frames, interval=50, blit=True)

    if save_path:
        anim.save(save_path, writer="pillow", fps=30)

    return anim


if __name__ == "__main__":
    mpl.rcParams["animation.embed_limit"] = 100.0

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
