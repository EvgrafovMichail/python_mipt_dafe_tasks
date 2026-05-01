import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def signal_calculation(modulation, t, fc):
    if not modulation:
        return np.sin(2 * np.pi * fc * t)
    return modulation(t) * np.sin(2 * np.pi * fc * t)


def set_style(axis):
    axis.set_title("Анимация сигнала", fontsize=17, fontweight="bold")
    axis.set_xlabel("Время (с)", fontsize=12, fontweight="bold")
    axis.set_ylabel("Амплитуда", fontsize=12, fontweight="bold")

    axis.legend()


def create_modulation_animation(
    modulation,
    fc,
    num_frames,
    plot_duration,
    time_step=0.001,
    animation_step=0.01,
    save_path="",
) -> FuncAnimation:
    figure, axis = plt.subplots(figsize=(10, 8))

    full_plot_duration = plot_duration + num_frames * animation_step
    t_full = np.arange(0, full_plot_duration, time_step)
    full_signal = signal_calculation(modulation, t_full, fc)

    line, *_ = axis.plot([], [], c="darkmagenta", label="Сигнал")

    def update_frame(frame_id):
        start_time = frame_id * animation_step  # для текущего кадра
        end_time = start_time + plot_duration

        start_time_index = int(start_time / time_step)
        end_time_index = start_time_index + int(plot_duration / time_step)

        t = t_full[start_time_index:end_time_index]
        signal = full_signal[start_time_index:end_time_index]

        line.set_data(t, signal)
        axis.set_xlim(start_time, end_time)
        axis.set_ylim(2 * np.min(signal), 2 * np.max(signal))
        return (line,)

    set_style(axis)

    animation = FuncAnimation(
        figure,
        update_frame,
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
    HTML(animation.to_jshtml())
