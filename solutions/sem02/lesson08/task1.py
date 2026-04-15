import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


class SignalModulation:
    def __init__(self, modulation, fc):
        self.modulation = modulation
        self.fc = fc

    def signal_function(self, t):
        formula = np.sin(2 * np.pi * self.fc * t)
        if self.modulation is None:
            return formula
        return self.modulation(t) * formula


class SignalDisplay:
    def __init__(
        self, signal, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
    ):
        self.signal = signal
        self.num_frames = num_frames
        self.plot_duration = plot_duration
        self.time_step = time_step
        self.animation_step = animation_step
        self.save_path = save_path
        self.figure = None
        self.axis = None
        self.line = None

    def animate(self):
        self._setup_plot()

        animation = FuncAnimation(
            self.figure, self._update_frame, frames=self.num_frames, blit=True
        )

        if self.save_path:
            self._save(animation)

        return animation

    def _generate_time(self, start):
        return np.arange(start, start + self.plot_duration, self.time_step)

    def _signal_function(self, t):
        return self.signal.signal_function(t)

    def _setup_plot(self):
        self.figure, self.axis = plt.subplots(figsize=(16, 9))
        (self.line,) = self.axis.plot([], [])

        self.axis.set_ylim(-1.5, 1.5)
        self.axis.set_xlabel("время (секунды)")
        self.axis.set_ylabel("амплитуда")

    def _update_plot(self, t, y):
        self.line.set_data(t, y)
        self.axis.set_xlim(t[0], t[-1])

    def _update_frame(self, frame):
        start = frame * self.animation_step

        t = self._generate_time(start)
        y = self._signal_function(t)

        self._update_plot(t, y)

        return (self.line,)

    def _save(self, anim):
        anim.save(self.save_path, writer="pillow", fps=52)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    signal = SignalModulation(modulation, fc)

    animator = SignalDisplay(
        signal=signal,
        num_frames=num_frames,
        plot_duration=plot_duration,
        time_step=time_step,
        animation_step=animation_step,
        save_path=save_path,
    )
    anim = animator.animate()
    plt.show()

    return anim


if __name__ == "__main__":

    def modulation_function(t):
        return np.cos(t * 6)

    num_frames = 150
    plot_duration = np.pi / 2
    time_step = 0.001
    animation_step = np.pi / 200
    fc = 5
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
