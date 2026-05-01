import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    def signal(t, modulation, fc):
        base_signal = np.sin(2 * np.pi * fc * t)
        if modulation is None:
            return base_signal
        return modulation(t) * base_signal

    figure, axis = plt.subplots(figsize=(12, 6))
    num_points = int(plot_duration / time_step) + 1
    time_segment = np.linspace(0, plot_duration, num_points)
    num_segment = signal(time_segment, modulation, fc)
    line, *_ = axis.plot(time_segment, num_segment, c="coral")
    result_duration = (num_frames - 1) * animation_step + plot_duration
    result_num_points = int(result_duration / time_step) + 1
    result_time = np.linspace(0, result_duration, result_num_points)
    total_signal = signal(result_time, modulation, fc)
    axis.set_xlim(0, plot_duration)
    ymax = 1.2 * np.max(np.abs(total_signal))
    axis.set_ylim(-ymax, ymax)

    def update(frame_id):
        start = frame_id * animation_step
        end = start + plot_duration
        start_index = int(start / time_step)
        end_index = start_index + num_points
        time_minisegment = result_time[start_index:end_index]
        signal_minisegment = total_signal[start_index:end_index]
        line.set_data(time_minisegment, signal_minisegment)
        axis.set_xlim(start, end)
        return (line,)

    animation = FuncAnimation(
        figure,
        update,
        frames=num_frames,
        interval=50,
        blit=False,
    )
    if save_path:
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
