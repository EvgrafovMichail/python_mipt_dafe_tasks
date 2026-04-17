import numpy as np
import matplotlib.pyplot as plt
from IPython.display import HTML
from matplotlib.animation import FuncAnimation


def create_modulation_animation(
    modulation, fc, num_frames, plot_duration, time_step=0.001, animation_step=0.01, save_path=""
) -> FuncAnimation:
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=1, color="#058D29")
    
    ax.set_xlim(0, plot_duration)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("Время (с)")
    ax.set_ylabel("Амплитуда")
    ax.set_title("Амплитудная модуляция" if modulation else "Несущий сигнал")
    ax.grid(True)

    def update(frame):
        start_time = frame * animation_step
        end_time = start_time + plot_duration
        
        t = np.arange(start_time, end_time, time_step)
        carrier = np.sin(2 * np.pi * fc * t)
        
        if modulation is not None:
            m_t = modulation(t)
            signal = m_t * carrier
        else:
            signal = carrier
            
        line.set_data(t, signal)
        ax.set_xlim(start_time, end_time)
        
        return line,

    anim = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

    if save_path:
        anim.save(save_path, writer='pillow')
    
    plt.close(fig) 
    return anim


if __name__ == "__main__":

    def modulation_function(t):
        return np.cos(t * 6)

    num_frames = 100
    plot_duration = np.pi / 2
    time_step = 0.001
    animation_step = np.pi / 200
    fc = 50
    save_path_with_modulation = "solutions/sem02/lesson08/modulated_signal.gif"

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
