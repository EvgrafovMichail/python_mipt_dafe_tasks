from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


class SignalAnimate:
    def __init__(self, fc, modulation, num_frames, plot_duration, time_step, animation_step, path):
        self.num_frames = num_frames
        self.plot_duration = plot_duration
        self.time_step = time_step
        self.animation_step = animation_step
        self.fc = fc
        self.modulation = modulation
        self.path = path

    def calcSig(self, t: np.array):
        signal = np.sin(2 * np.pi * self.fc * t)
        if self.modulation is not None:
            return signal * self.modulation(t)
        return signal

    def update(self, frame, *, line: plt.Line2D):
        frameStart = frame * self.animation_step
        frameEnd = frameStart + self.plot_duration
        t = np.arange(frameStart, frameEnd, self.time_step)
        signal = self.calcSig(t)
        line.set_data(t, signal)
        line.axes.set_xlim(frameStart, frameEnd)
        return (line,)

    def animate(self):
        figure, axis = plt.subplots(figsize=(16, 9))
        (line,) = axis.plot([], [], color="red")
        axis.set_ylim(-2, 2)
        axis.set_title("Анимация модулированного сигнала")
        axis.set_ylabel("Амплитуда")
        axis.set_xlabel("Время")
        animation = FuncAnimation(
            figure,
            partial(self.update, line=line),
            frames=self.num_frames,
            interval=20,
        )
        if self.path != "":
            animation.save(self.path, writer="pillow", fps=24)
        return animation


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    sig = SignalAnimate(
        fc, modulation, num_frames, plot_duration, time_step, animation_step, save_path
    )
    return sig.animate()


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
