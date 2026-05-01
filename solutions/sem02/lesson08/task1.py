import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def calculate(t: np.ndarray, modulation, fc) -> np.ndarray:
    if modulation is not None:
        return np.sin(2 * np.pi * fc * t) * modulation(t)
    return np.sin(2 * np.pi * fc * t)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    abscissa = np.arange(0, plot_duration, time_step)

    figure, axis = plt.subplots(figsize=(16, 9))
    axis: plt.Axes

    line, *_ = axis.plot(
        abscissa,
        np.sin(abscissa) * modulation(abscissa),
        c="royalblue",
    )

    def update_frame(frame_id: int) -> tuple[plt.Line2D]:
        t = abscissa + frame_id * animation_step
        ordinates = calculate(t, modulation, fc)

        axis.set_ylim(-2.0, 2.0)
        axis.set_xlim(t.min(), t.max())
        line.set_data(t, ordinates)

        return (line,)

    animation = FuncAnimation(
        figure,
        update_frame,
        frames=num_frames,
        interval=50,
        blit=False,
    )

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
