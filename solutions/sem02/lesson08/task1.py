
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def generate_signal(t: np.ndarray, modulation, fc: float) -> np.ndarray:
    carrier = np.sin(2 * np.pi * fc * t)

    if modulation is None:
        return carrier

    return modulation(t) * carrier


def get_time_window(start: float, duration: float, step: float) -> np.ndarray:
    return np.arange(start, start + duration, step)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    fig, ax = plt.subplots()

    (line,) = ax.plot([], [], lw=2, label="Сигнал")
    ax.set_xlim(0, plot_duration)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title("Анимация модулированного сигнала")
    ax.set_xlabel("Время(с)")
    ax.set_ylabel("Амплитуда")
    ax.legend()

    def init():
        line.set_data([], [])
        return (line,)

    def update(frame):
        t_start = frame * animation_step
        t = get_time_window(t_start, plot_duration, time_step)

        s = generate_signal(t, modulation, fc)
        line.set_data(t, s)
        ax.set_xlim(t_start, t_start + plot_duration)

        return (line,)

    animation = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)

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
