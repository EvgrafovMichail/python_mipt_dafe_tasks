import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    t_frame = np.arange(0, plot_duration, time_step)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, plot_duration)
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True, alpha=0.3)
    (line,) = ax.plot([], [], lw=2, color="#c660a2")

    def update_frame(frame_id: int):
        t_start = frame_id * animation_step
        t = t_start + t_frame
        carrier = np.sin(2 * np.pi * fc * t)
        if modulation is not None:
            signal = modulation(t) * carrier
        else:
            signal = carrier
        line.set_data(t_frame, signal)
        return (line,)

    animation = FuncAnimation(
        fig, update_frame, frames=num_frames, interval=50, blit=True, repeat=True
    )
    if save_path:
        animation.save(save_path, writer="pillow", fps=20)
        print("done animation")
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
