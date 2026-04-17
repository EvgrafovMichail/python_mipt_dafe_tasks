import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def get_modulated_signal(t, fc, modulation):
    carrier = np.sin(2 * np.pi * fc * t)
    m_t = modulation(t) if modulation is not None else 1.0
    return m_t * carrier


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:

    fig, ax = plt.subplots(figsize=(8, 5))
    (line,) = ax.plot([], [], lw=1.5, label="Сигнал")

    ax.set_ylim(-2.0, 2.0)
    ax.set_xlabel("Время (с)")
    ax.set_ylabel("Амплитуда")
    ax.set_title("Анимация модулированного сигнала")
    ax.legend(loc="upper right")
    ax.grid(True, linestyle="-", alpha=0.3)

    def init():
        """Инициализация пустого кадра."""
        line.set_data([], [])
        return (line,)

    def update(frame):
        t_start = frame * animation_step
        t_end = t_start + plot_duration

        t = np.arange(t_start, t_end, time_step)
        y = get_modulated_signal(t, fc, modulation)

        line.set_data(t, y)
        ax.set_xlim(t_start, t_end)
        return (line,)

    anim = FuncAnimation(fig, update, frames=num_frames, init_func=init, interval=50, blit=True)

    if save_path:
        anim.save(save_path, writer="pillow")
        plt.close(fig)

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
