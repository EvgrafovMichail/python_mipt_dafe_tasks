from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def calculate_signal(t_start, plot_duration, time_step, fc, modulation):
    t = np.arange(t_start, t_start + plot_duration, time_step)
    m_t = modulation(t) if modulation is not None else np.ones_like(t)
    s_t = m_t * np.sin(2 * np.pi * fc * t)
    return t, s_t


def update_frame(frame, line, ax, fc, modulation, plot_duration, time_step, animation_step):
    t_start = frame * animation_step
    t, s_t = calculate_signal(t_start, plot_duration, time_step, fc, modulation)
    line.set_data(t, s_t)
    ax.set_xlim(t_start, t_start + plot_duration)
    return (line,)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    fig, ax = plt.subplots(figsize=(10, 4))
    (line,) = ax.plot([], [], lw=1.5)

    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("Время (с)")
    ax.set_ylabel("Амплитуда")
    ax.set_title(f"Амплитудная модуляция (fc={fc} Гц)")
    ax.grid(True, linestyle="--", alpha=0.6)

    frame_renderer = partial(
        update_frame,
        line=line,
        ax=ax,
        fc=fc,
        modulation=modulation,
        plot_duration=plot_duration,
        time_step=time_step,
        animation_step=animation_step,
    )

    animation = FuncAnimation(fig, frame_renderer, frames=num_frames, interval=50, blit=False)

    if save_path:
        animation.save(save_path, writer="pillow")
        plt.close(fig)

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
