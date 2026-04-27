from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def create_modulation_animation(
    modulation,  # Функция модуляции
    fc,  # Частота несущего сигнала
    num_frames,  # Количество кадров, которые будут сохранены в анимацию
    plot_duration,  # длительность интервала времени до зацикливания
    time_step=0.001,  # Промежуток времени между соседними вычисленными точками сигнала
    animation_step=0.01,  # время, которое прибавляется к оси за кадр
    save_path="",
) -> FuncAnimation:
    figure, axis = plt.subplots(figsize=(16, 9))
    axis.set_xlabel("Время (с)", fontsize=20)
    axis.set_ylabel("Амплитуда", fontsize=20)
    axis.text(
        0.98,
        0.98,
        "Модулированный сигнал",
        transform=axis.transAxes,
        ha="right",
        va="top",
        fontsize=14,
        bbox=dict(facecolor="white", alpha=0.5, edgecolor="black"),
    )
    x_values = np.arange(0, plot_duration, time_step)
    if modulation is None:
        modulation_multiplier = 1.0
    else:
        modulation_multiplier = modulation(x_values)
    y_values_start = modulation_multiplier * np.sin(2 * np.pi * fc * x_values)
    (line_start,) = axis.plot(x_values, y_values_start, lw=1, c="purple")

    axis.set_xlim(x_values.min(), x_values.max())
    axis.set_ylim(-1.5, 1.5)

    def update_frame(frame_id: int):
        t = x_values + animation_step * frame_id
        if modulation is None:
            modulation_multiplier = 1.0
        else:
            modulation_multiplier = modulation(t)
        y_values_new = modulation_multiplier * np.sin(2 * np.pi * fc * t)
        line_start.set_data(t, y_values_new)
        axis.set_xlim(t.min(), t.max())
        return line_start, axis

    anim = FuncAnimation(figure, update_frame, frames=num_frames, interval=50, blit=False)

    if save_path:
        anim.save(save_path, writer="pillow")

    return anim


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
