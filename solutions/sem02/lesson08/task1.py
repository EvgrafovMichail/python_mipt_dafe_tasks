from functools import partial
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    fig, ax = plt.subplots(figsize=(10, 6))

    total_duration = plot_duration + num_frames * animation_step
    t_full = np.arange(0, total_duration, time_step)
    carrier_full = np.cos(2 * np.pi * fc * t_full)
    modulating_full = modulation(t_full)
    signal_full = modulating_full * carrier_full

    window_samples = int(plot_duration / time_step)
    t_window = t_full[:window_samples]
    signal_window = signal_full[:window_samples]
    line = ax.plot(t_window, signal_window)[0]

    ax.set_xlim(0, plot_duration)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("Время (с)")
    ax.set_ylabel("Амплитуда")
    ax.set_title("Анимация модулированного сигнала")
    ax.grid(True)

    def update_frame(frame, t_full, signal_full, window_samples, time_step, plot_duration):
        current_shift = frame * animation_step
        start_idx = int(current_shift / time_step)
        if start_idx + window_samples >= len(t_full):
            start_idx = 0
        end_idx = start_idx + window_samples
        t_current = t_full[start_idx:end_idx]
        signal_current = signal_full[start_idx:end_idx]
        line.set_xdata(t_current)
        line.set_ydata(signal_current)
        ax.set_xlim(t_current[0], t_current[-1])
        return line

    update_with_params = partial(
        update_frame,
        t_full=t_full,
        signal_full=signal_full,
        window_samples=window_samples,
        time_step=time_step,
        plot_duration=plot_duration,
    )

    animation = FuncAnimation(
        fig=fig, func=update_with_params, frames=num_frames, interval=50, repeat=True, blit=False
    )
    animation.save(save_path, writer="pillow", fps=20)
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

    plt.show()
