import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


class SignalAnimator:
    def __init__(self, modulation, fc, num_frames, plot_duration, animation_step) -> None:
        self.modulation = modulation
        self.fc = fc
        self.plot_duration = plot_duration
        self.animation_step = animation_step
        self.fig, self.ax = plt.subplot()
        (self.line,) = self.ax.plot([], [], lw=2, label="Сигнал")

    def graphics_design(self):
        self.ax.set_title("Анимация модулированного сигнала")
        self.ax.set_xlim(0, self.plot_duration)
        self.ax.set_xlabel("Время (с)")
        self.ax.set_ylim(-2, 2)
        self.ax.set_ylabel("Амплитуда")
        self.ax.legend()

    def modulated_signal_formula(self, points):
        return self.modulation(points) * np.cos(2 * np.pi * fc * points)

    def frame_update(self, frame):
        start_time = frame * self.animation_step
        end_time = start_time + plot_duration

        points = np.linspace(start_time, end_time, 1000)
        signal = self.modulation(points) * np.cos(2 * np.pi * fc * points)
        self.line.set_data(points, signal)
        self.ax.set_xlim(start_time, end_time)
        return self.line


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    fig, ax = plt.subplots()
    ax.set_title("Анимация модулированного сигнала")
    (line,) = ax.plot([], [], lw=2)

    x = np.linspace(0, 10, 1000)
    y = np.cos(x)

    line.set_data(x, y)

    ax.set_xlim(0, plot_duration)
    ax.set_xlabel("Время (с)")
    ax.set_ylim(-2, 2)
    ax.set_ylabel("Амплитуда")
    ax.legend(["Сигнал"])

    def update(frame):
        start_time = frame * animation_step
        end_time = start_time + plot_duration

        points = np.linspace(start_time, end_time, 1000)
        signal = modulation(points) * np.cos(2 * np.pi * fc * points)
        line.set_data(points, signal)
        ax.set_xlim(start_time, end_time)
        return line

    return FuncAnimation(fig, update, frames=num_frames, interval=30)


if __name__ == "__main__":

    def modulation_function(t):
        return np.cos(t * 6)

    num_frames = 200
    plot_duration = np.pi / 2
    time_step = 0.01
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
