from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    abscissa = np.arange(0, plot_duration, time_step)

    def signal(abscissa, modulation, fc):
        f = np.sin(2 * np.pi * fc * abscissa)

        if modulation is None:
            return f
        else:
            return modulation(abscissa) * f

    figure, axis = plt.subplots(figsize=(16, 9))
    axis.set_xlim(0, plot_duration)

    line, *_ = axis.plot(
        abscissa,
        signal(abscissa, modulation, fc),
        c="deeppink",
    )

    def update_frame(
        frame_id: int,
    ) -> tuple[plt.Line2D]:
        new_x = abscissa + frame_id * animation_step
        sign = signal(new_x, modulation, fc)
        line.set_ydata(sign)

        return (line,)

    animation = FuncAnimation(
        figure,
        update_frame,
        frames=num_frames,
        interval=50,
        blit=True,
    )

    if save_path:
        animation.save("func.gif", writer="pillow", fps=24)

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
