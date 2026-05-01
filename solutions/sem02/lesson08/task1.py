import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def _build_signal(
    time_values: np.ndarray,
    modulation,
    carrier_frequency: float,
) -> np.ndarray:
    if modulation is None:
        modulation_values = np.ones_like(time_values)
    else:
        try:
            modulation_values = modulation(time_values)
        except TypeError:
            modulation_values = np.vectorize(modulation)(time_values)

    modulation_values = np.asarray(modulation_values, dtype=float)
    return modulation_values * np.sin(2 * np.pi * carrier_frequency * time_values)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    # ваш код
    local_time = np.arange(0, plot_duration, time_step)

    max_time = plot_duration + max(num_frames - 1, 0) * animation_step
    full_time = np.arange(0, max_time + time_step, time_step)
    full_signal = _build_signal(full_time, modulation, fc)

    max_amplitude = float(np.max(np.abs(full_signal)))
    if max_amplitude == 0:
        max_amplitude = 1.0

    figure, axis = plt.subplots(figsize=(10, 4))
    axis: plt.Axes

    axis.set_xlim(0, plot_duration)
    axis.set_ylim(-1.2 * max_amplitude, 1.2 * max_amplitude)
    axis.set_title("Амплитудно-модулированный сигнал")
    axis.set_xlabel("Время, с")
    axis.set_ylabel("Амплитуда")
    axis.grid(True, alpha=0.3)

    (line,) = axis.plot([], [], linewidth=2)

    def update(frame_id: int):
        current_time = local_time + frame_id * animation_step
        signal_values = _build_signal(current_time, modulation, fc)
        line.set_data(local_time, signal_values)
        return [line]

    animation = FuncAnimation(
        figure,
        update,
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
    save_path_with_modulation = "solutions/sem02/lesson08/modulated_signal.gif"

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
