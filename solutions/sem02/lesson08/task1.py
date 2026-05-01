from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def update_frame(
        frame_id: int,
        *,
        line: plt.Line2D,
        axis: plt.Axes,
        modulation,
        fc: float,
        plot_duration: float,
        time_step: float,
        animation_step: float,
) -> tuple[plt.Line2D]:
    time_start = frame_id * animation_step
    time_end = time_start + plot_duration
    times = np.arange(time_start, time_end, time_step)

    modulated_times = modulation(times) if modulation is not None else np.ones_like(times)
    ordinates = modulated_times * np.sin(2 * np.pi * fc * times)

    line.set_data(times, ordinates)
    axis.set_xlim(time_start, time_end)
    return line,


def create_modulation_animation(
    modulation, 
    fc, 
    num_frames, 
    plot_duration, 
    time_step=0.001, 
    animation_step=0.01,
    save_path=""
) -> FuncAnimation:
    figure, axis = plt.subplots(figsize=(16, 9))
    axis.set_ylim(-2, 2)
    axis.set_xlabel("Время (с)")
    axis.set_ylabel("Амплитуда")

    line, *_ = axis.plot([], [], c="red", lw=2)

    animation = FuncAnimation(
        figure,
        partial(
            update_frame,
            line=line,
            axis=axis,
            modulation=modulation,
            fc=fc,
            plot_duration=plot_duration,
            time_step=time_step,
            animation_step=animation_step
        ),
        frames=num_frames,
        interval=50,
        blit=True,
    )

    if save_path:
        animation.save(save_path, writer='pillow')
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