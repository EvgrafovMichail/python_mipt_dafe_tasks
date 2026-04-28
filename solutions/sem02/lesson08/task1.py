from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def compute_signal(t: np.ndarray, modulation, fc: float) -> np.ndarray:
    carrier = np.sin(2 * np.pi * fc * t)
    if modulation is not None:
        return modulation(t) * carrier
    return carrier


def update_frame(frame: int, *, line, ax, modulation, fc, plot_duration, animation_step, time_step):
    t_start = frame * animation_step
    t = np.arange(t_start, t_start + plot_duration, time_step)
    signal = compute_signal(t, modulation, fc)

    line.set_data(t, signal)
    ax.set_xlim(t[0], t[-1])

    max_amp = np.max(np.abs(signal)) if t.size > 0 else 1.0
    ax.set_ylim(-max_amp * 1.1, max_amp * 1.1)
    return (line,)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    fig, ax = plt.subplots(figsize=(9, 5))
    (line,) = ax.plot([], [], lw=2, color="royalblue")
    ax.set_xlabel("Время (с)")
    ax.set_ylabel("Амплитуда")
    ax.grid(True)

    update_callback = partial(
        update_frame,
        line=line,
        ax=ax,
        modulation=modulation,
        fc=fc,
        plot_duration=plot_duration,
        animation_step=animation_step,
        time_step=time_step,
    )

    anim = FuncAnimation(fig, update_callback, frames=num_frames, blit=False, interval=50)

    if save_path:
        anim.save(save_path, writer="pillow", fps=24)

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
