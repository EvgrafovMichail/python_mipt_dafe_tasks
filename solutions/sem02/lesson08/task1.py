from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def create_modulation_animation(
    modulation, 
    fc, 
    num_frames, 
    plot_duration, 
    time_step=0.001, 
    animation_step=0.01,
    save_path=""
) -> FuncAnimation:
    abscissa = np.arange(0, plot_duration, time_step)

    if modulation is None:
        def modulation(t):
            return np.ones_like(t)


    def update_frame(
            frame_id: int,
            *,
            line: plt.Line2D,
    ) -> tuple[plt.Line2D]:
        n_abscissa = abscissa + frame_id * animation_step
        ordinates = modulation(n_abscissa) * np.sin(2 * np.pi * fc * n_abscissa)
        line.set_data(n_abscissa, ordinates)
        axis.set_xlim(n_abscissa.min(), n_abscissa.max())
        return line,

    figure, axis = plt.subplots(figsize=(16, 9))
    axis: plt.Axes

    axis.set_xlim(abscissa.min(), abscissa.max())
    line, *_ = axis.plot(
        abscissa,
        modulation(abscissa) * np.sin(2* np.pi * fc *abscissa),
        c="green",
    )

    animation = FuncAnimation(
        figure,
        partial(update_frame, line=line),
        frames=num_frames,
        interval=animation_step,
        blit=False,
    )
    if save_path != "":
        animation.save(save_path, writer="pillow")

    plt.close(figure)
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
        save_path=save_path_with_modulation
    )
    HTML(animation.to_jshtml())