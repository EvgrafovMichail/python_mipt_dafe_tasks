
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation, PillowWriter


class ModulationAnimation:
    def __init__(
        self,
        modulation,
        fc,
        num_frames,
        plot_duration,
        time_step=0.001,
        animation_step=0.01,
        save_path="",
    ):
        pass


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    figure, axis = plt.subplots(figsize=(6, 4))

    axis.set_title("Анимация моудлированного сигнала")
    axis.set_xlabel("Время (с)")
    axis.set_ylabel("Амплитуда")

    axis.set_ylim(-2, 2)

    plot = axis.plot([], [])[0]

    axis.legend(["Сигнал"])

    if modulation is None:
        modulation = lambda t: 1

    def callback(frame_id):
        from_t = frame_id * animation_step
        to_t = from_t + plot_duration

        abscissa = np.arange(from_t, to_t, time_step)
        ordinate = modulation(abscissa) * np.sin(2 * np.pi * fc * abscissa)

        axis.set_xlim(from_t, to_t)
        plot.set_data(abscissa, ordinate)

        return [plot]

    animation = FuncAnimation(figure, callback, frames=num_frames, interval=20, blit=False)

    if save_path:
        animation.save(save_path, writer=PillowWriter(fps=50))

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
