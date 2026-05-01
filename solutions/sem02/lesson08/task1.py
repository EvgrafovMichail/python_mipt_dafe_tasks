import matplotlib.pyplot as plt
import numpy as np

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
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.set_xlabel("Время, с")
    ax.set_ylabel("Амплитуда")
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-2, 2)
    
    line, = ax.plot([], [], lw=2, color="red")
    
    def init():
        line.set_data([], [])
        ax.set_xlim(0, plot_duration)
        return line,
    
    def update(frame):
        t_start = frame * animation_step
        t_end = t_start + plot_duration
        
        t = np.arange(t_start, t_end, time_step)
        carrier = np.sin(2 * np.pi * fc * t)
        
        if modulation is not None:
            signal = modulation(t) * carrier
        else:
            signal = carrier
        
        line.set_data(t, signal)
        ax.set_xlim(t_start, t_end)
        
        return line,
    
    anim = FuncAnimation(
        fig, 
        update, 
        frames=num_frames, 
        init_func=init, 
        blit=True,
        interval=animation_step * 1000
    )
    
    if save_path:
        anim.save(save_path, writer="pillow", fps= 1.0 / animation_step)
    
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