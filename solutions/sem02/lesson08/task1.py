
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
    def signal(t):
        carrier = np.sin(2 * np.pi * fc * t)
        return carrier if modulation is None else modulation(t) * carrier
    
    fig, ax = plt.subplots(figsize=(12, 6))
    num_points = int(plot_duration / time_step) + 1
    time_segment = np.linspace(0, plot_duration, num_points)
    
    line, = ax.plot(time_segment, signal(time_segment), 'b-', lw=2)
    
    if modulation is not None:
        envelope, = ax.plot(time_segment, modulation(time_segment), 'r--', alpha=0.7)
    
    total_duration = (num_frames - 1) * animation_step + plot_duration
    total_points = int(total_duration / time_step) + 1
    total_time = np.linspace(0, total_duration, total_points)
    total_signal = signal(total_time)
    
    ax.set_xlim(0, plot_duration)
    ax.set_ylim(-1.2 * np.max(np.abs(total_signal)), 1.2 * np.max(np.abs(total_signal)))
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title('Modulated Signal')
    
    def update(frame):
        start = frame * animation_step
        idx = int(start / time_step)
        line.set_data(total_time[idx:idx+num_points], total_signal[idx:idx+num_points])
        ax.set_xlim(start, start + plot_duration)
        if modulation is not None:
            envelope.set_data(
                total_time[idx:idx+num_points], 
                modulation(total_time[idx:idx+num_points])
            )
        return (line,)
    
    anim = FuncAnimation(fig, update, frames=num_frames, interval=50)
    
    if save_path:
        anim.save(save_path, writer='pillow')
    
    return anim


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