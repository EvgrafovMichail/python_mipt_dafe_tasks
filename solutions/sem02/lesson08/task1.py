import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    def generate_signal(t_values: np.ndarray) -> np.ndarray:
        carrier = np.sin(2 * np.pi * fc * t_values)

        if modulation is None:
            return carrier

        modulation_values = modulation(t_values)
        return modulation_values * carrier

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, plot_duration)
    ax.set_ylim(-2.5, 2.5)
    ax.set_xlabel("Время (с)")
    ax.set_ylabel("Амплитуда")
    ax.grid(True, alpha=0.3, color="gray")

    title = "Амплитудно-модулированный сигнал" if modulation is not None else "Несущий сигнал"
    ax.set_title(f"{title}\nНесущая частота: {fc} Гц")

    (line,) = ax.plot([], [], "m-", linewidth=1.5)

    time_text = ax.text(
        0.02,
        0.95,
        "",
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
    )

    def init():
        line.set_data([], [])
        time_text.set_text("")
        return line, time_text

    def update(frame):
        current_time = frame * animation_step

        num_points = int(plot_duration / time_step)
        t_values = np.linspace(current_time, current_time + plot_duration, num_points)

        signal_values = generate_signal(t_values)

        line.set_data(t_values - current_time, signal_values)

        time_text.set_text(f"Время: {current_time:.3f} с")

        return line, time_text

    anim = FuncAnimation(fig, update, init_func=init, frames=num_frames, interval=50, blit=True)

    if save_path:
        try:
            if not save_path.endswith(".gif"):
                save_path += ".gif"

            print(f"Сохранение анимации в {save_path}...")
            anim.save(save_path, writer="pillow", fps=20)
            print(f"Анимация успешно сохранена в {save_path}")
        except Exception as e:
            print(f"Ошибка при сохранении анимации: {e}")
            print("Убедитесь, что установлен pillow: pip install pillow")

    return anim


if __name__ == "__main__":

    def modulation_function(t):
        return np.cos(t * 6)

    num_frames = 100
    plot_duration = np.pi / 2
    time_step = 0.001
    animation_step = np.pi / 200
    fc = 50
    save_path_with_modulation = "./solutions/sem02/lesson08/gifs/modulated_signal.gif"

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
