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
    def update_frame(
            frame_number,
            *,
            line: plt.Line2D,
            axis: plt.Axes,
            abscissa: np.ndarray
            ) -> tuple[plt.Line2D, plt.Axes]:
        t_start = frame_number * time_step
        t_end = t_start + plot_duration
        abscissa = np.linspace(t_start, t_end, int(plot_duration / time_step))
        ordinate = modulation(abscissa) * np.sin(2 * np.pi * fc * abscissa)
        line.set_data(abscissa, ordinate)
        axis.set_xlim(t_start, t_end)
        return line, axis
    abscissa = np.linspace(0, plot_duration, int(plot_duration / time_step))
    figure, axis = plt.subplots()
    axis.set_xlabel("Время, с")
    axis.set_ylabel("Амплитуда")
    axis.set_title("Модулированный сигнал")
    axis.set_xlim(0, plot_duration)
    axis.set_ylim(min(modulation(abscissa)) - 1, max(modulation(abscissa)) + 1)
    line, = axis.plot(
        abscissa,
        modulation(abscissa) * np.sin(2 * np.pi * fc * abscissa)
        )
    animation = FuncAnimation(
        figure,
        partial(update_frame, line=line, axis=axis, abscissa=abscissa),
        frames=num_frames,
        interval=animation_step * 1000
    )
    if save_path != "":
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
        save_path=save_path_with_modulation
    )
    HTML(animation.to_jshtml())