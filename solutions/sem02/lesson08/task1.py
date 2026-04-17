from functools import partial
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def _calculate_signal(time_array, modulation, fc):
    carrier = np.sin(2 * np.pi * fc * time_array)

    if modulation is not None:
        return modulation(time_array) * carrier
    else:
        return carrier


def _update_frame(frame_id, line, axis, modulation, fc, plot_duration, time_step, animation_step):
    start_time = frame_id * animation_step
    end_time = start_time + plot_duration

    t = np.arange(start_time, end_time, time_step)
    y = _calculate_signal(t, modulation, fc)

    line.set_data(t, y)
    axis.set_xlim(start_time, end_time)
    axis.set_ylim(-2.5, 2.5)

    return (line,)


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    fig, ax = plt.subplots(figsize=(10, 5))

    fig.patch.set_facecolor(
        "#004488"
    )  # рассцветку фона и линий нагло украл из инженерных чертежей из мультов, она очень стильная
    ax.set_facecolor("#004488")

    ax.set_title("Amplitude Modulation Signal", fontsize=14, fontweight="bold", color="white")
    ax.set_xlabel("Time, [s]", color="white")
    ax.set_ylabel("Amplitude", color="white")

    ax.grid(True, color="gray", linestyle="--", alpha=0.5)

    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_edgecolor("white")

    (line,) = ax.plot([], [], lw=2, color="white")

    update_with_args = partial(
        _update_frame,
        line=line,
        axis=ax,
        modulation=modulation,
        fc=fc,
        plot_duration=plot_duration,
        time_step=time_step,
        animation_step=animation_step,
    )

    anim = FuncAnimation(
        fig, update_with_args, frames=num_frames, interval=animation_step * 1000, blit=False
    )

    if save_path != "":
        anim.save(save_path, writer="pillow")
    else:
        pass

    return anim


if __name__ == "__main__":

    def modulation_function(t):
        return np.cos(t * 6)

    num_frames = 100
    plot_duration = np.pi / 2
    time_step = 0.001
    animation_step = np.pi / 200
    fc = 50
    save_path_with_modulation = "blueprint_signal.gif"

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
