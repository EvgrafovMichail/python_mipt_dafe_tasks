from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image
from matplotlib.animation import FuncAnimation

plt.style.use("default")


class ModulatedSignal:
    def __init__(
        self,
        modulation: Callable,
        fc: float,
    ) -> None:
        if modulation != None:
            self.modulation = modulation
        else:
            self.modulation = lambda abscissa: 1
        self.fc = fc

    def __call__(
        self,
        abscissa: np.ndarray,
    ) -> np.ndarray:
        modulating = self.modulation(abscissa)
        carrier = np.sin(2 * np.pi * self.fc * abscissa)
        modulated = modulating * carrier
        return modulated


def axis_init(
    plot_duration: float,
    time_step: float,
    signal: Callable,
) -> tuple[plt.Figure, plt.Axes, np.ndarray]:
    figure, axis = plt.subplots(
        figsize=(6.4, 4.8),
        facecolor="royalblue",
    )

    amount = int(plot_duration / time_step)
    abscissa = np.linspace(0, plot_duration, amount)

    ordinates = signal(abscissa)
    axis.set_ylim(ordinates.min() - 1.5, ordinates.max() + 1.5)

    axis.set_title(
        "Анимация модулированного сигнала",
        fontsize=17,
        color="white",
        pad=20,
    )
    axis.set_xlabel(
        "Время (с)",
        fontsize=14,
        color="white",
        labelpad=7,
    )
    axis.set_ylabel(
        "Амплитуда",
        fontsize=14,
        color="white",
        labelpad=7,
    )
    axis.plot(
        abscissa,
        ordinates,
        c="royalblue",
        label="Сигнал",
    )

    plt.legend()
    return figure, axis, abscissa


class FrameUpdater:
    def __init__(
        self,
        step: float,
        axis: plt.Axes,
        abscissa: np.ndarray,
        signal: Callable,
    ) -> None:
        self.step = step
        self.abscissa = abscissa
        self.axis = axis
        self.signal = signal

    def __call__(
        self,
        frame_id: int,
    ) -> tuple[plt.Line2D]:
        step = self.step
        abscissa = self.abscissa
        axis = self.axis
        signal = self.signal

        lines = axis.get_lines()
        line = lines[0]
        x_data = abscissa + step * frame_id
        y_data = signal(x_data)
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        axis.set_xlim(x_data.min(), x_data.max())

        return lines


def create_modulation_animation(
    modulation: Callable,
    fc: float,
    num_frames: int,
    plot_duration: float,
    time_step=0.001,
    animation_step=0.01,
    save_path="",
) -> FuncAnimation:

    modulated_signal = ModulatedSignal(
        modulation,
        fc,
    )

    figure, axis, abscissa = axis_init(
        plot_duration,
        time_step,
        modulated_signal,
    )

    updater = FrameUpdater(
        animation_step,
        axis,
        abscissa,
        modulated_signal,
    )

    animation = FuncAnimation(
        figure,
        updater,
        frames=num_frames,
        interval=1000 * animation_step,
        blit=True,
    )
    if save_path != "":
        animation.save(
            save_path,
            writer="pillow",
            fps=30,
        )

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

Image(save_path_with_modulation)
