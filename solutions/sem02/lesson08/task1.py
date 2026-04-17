from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def update_frame(
    frame_id: int,
    *,
    line: plt.Line2D,
    abscissa: np.ndarray,
    axis: plt.Axes,
    func,
    animation_step,
) -> tuple[plt.Line2D]:
    shift = frame_id * animation_step
    ordinate = func(abscissa + shift)
    line.set_data(abscissa + shift, ordinate)
    axis.set_xlim(abscissa.min() + shift, abscissa.max() + shift)

    return line, axis


def function(
    modulation,
    fc,
):
    def wrapper(abscissa: np.ndarray):
        ordinate = modulation(abscissa) * np.sin(2 * np.pi * fc * abscissa)

        return ordinate

    return wrapper


def modulation_wraper(_):
    return 1


def create_modulation_animation(
    modulation,
    fc,
    num_frames,
    plot_duration,
    time_step=0.001,
    animation_step=0.01,
    save_path="",
) -> FuncAnimation:
    if not modulation:
        modulation = modulation_wraper

    num_points = int(plot_duration / time_step)
    abscissa = np.linspace(0, plot_duration, num_points)

    figure, axis = plt.subplots(figsize=(16, 9))
    axis: plt.Axes
    func = function(modulation, fc)
    ordinate = func(abscissa)

    axis.set_xlim(abscissa.min(), abscissa.max())
    line, *_ = axis.plot(abscissa, ordinate, c="royalblue")

    animation = FuncAnimation(
        figure,
        partial(
            update_frame,
            line=line,
            abscissa=abscissa,
            axis=axis,
            func=func,
            animation_step=animation_step,
        ),
        frames=num_frames,
        interval=animation_step * 1000,
        blit=False,
    )

    if save_path:
        animation.save(save_path, writer="pillow", fps=1 // animation_step)

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
    plt.show()
