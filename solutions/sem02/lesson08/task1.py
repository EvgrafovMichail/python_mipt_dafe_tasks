from functools import partial
from typing import Callable, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

plt.rcParams["animation.embed_limit"] = 50.0


def calculate_signal(
    t: np.ndarray, modulation: Optional[Callable[[np.ndarray], np.ndarray]], fc: float
) -> np.ndarray:
    """Вычисляет значения модулированного сигнала."""
    carrier = np.sin(2 * np.pi * fc * t)
    if modulation is None:
        return carrier
    return modulation(t) * carrier


def generate_frame_data(
    frame_idx: int,
    plot_duration: float,
    time_step: float,
    animation_step: float,
    modulation: Optional[Callable[[np.ndarray], np.ndarray]],
    fc: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """Генерирует массив времени и сигнала для конкретного кадра."""
    start_time = frame_idx * animation_step
    end_time = start_time + plot_duration
    num_points = int(plot_duration / time_step)

    t = np.linspace(start_time, end_time, num_points)
    signal = calculate_signal(t, modulation, fc)
    return t, signal


def create_canvas(plot_duration: float) -> Tuple[plt.Figure, plt.Axes, plt.Line2D]:
    """Создает полотно для графика и инициализирует линию."""
    figure, axis = plt.subplots(figsize=(16, 9))
    axis.set_xlim(0, plot_duration)
    axis.set_ylim(-1.5, 1.5)
    line, *_ = axis.plot([], [], c="pink")
    return figure, axis, line


def update_frame(
    frame_idx: int,
    line: plt.Line2D,
    axis: plt.Axes,
    plot_duration: float,
    time_step: float,
    animation_step: float,
    modulation: Optional[Callable[[np.ndarray], np.ndarray]],
    fc: float,
) -> Tuple[plt.Line2D]:
    """Обновляет данные линии и границы осей на каждом кадре."""
    t, signal = generate_frame_data(
        frame_idx, plot_duration, time_step, animation_step, modulation, fc
    )

    line.set_data(t, signal)
    axis.set_xlim(t.min(), t.max())

    return (line,)


def build_animation(
    figure: plt.Figure,
    line: plt.Line2D,
    axis: plt.Axes,
    num_frames: int,
    plot_duration: float,
    time_step: float,
    animation_step: float,
    modulation: Optional[Callable[[np.ndarray], np.ndarray]],
    fc: float,
) -> FuncAnimation:
    """Создает объект анимации."""
    interval_ms = animation_step

    frame_updater = partial(
        update_frame,
        line=line,
        axis=axis,
        plot_duration=plot_duration,
        time_step=time_step,
        animation_step=animation_step,
        modulation=modulation,
        fc=fc,
    )

    return FuncAnimation(figure, frame_updater, frames=num_frames, interval=interval_ms, blit=False)


def save_animation_to_file(animation: FuncAnimation, save_path: str) -> None:
    """Сохраняет анимацию в файл gif."""
    if save_path:
        animation.save(save_path, writer="pillow")


def create_modulation_animation(
    modulation: Optional[Callable[[np.ndarray], np.ndarray]],
    fc: float,
    num_frames: int,
    plot_duration: float,
    time_step: float = 0.001,
    animation_step: float = 0.01,
    save_path: str = "",
) -> FuncAnimation:
    """Оркестратор: координирует создание, отрисовку и сохранение анимации."""
    figure, axis, line = create_canvas(plot_duration)

    animation = build_animation(
        figure, line, axis, num_frames, plot_duration, time_step, animation_step, modulation, fc
    )

    save_animation_to_file(animation, save_path)

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
