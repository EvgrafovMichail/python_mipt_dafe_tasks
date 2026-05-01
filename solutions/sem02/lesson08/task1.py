from functools import partial

import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.set_xlim(0, plot_duration)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('Zeit (time) (s)', fontsize=12)
    ax.set_ylabel('Amplitude', fontsize=12)
    ax.set_title('Amplitudenmoduliertes Signal\n(Amplitude-modulated signal)', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    
    frame_time = np.arange(0, plot_duration, time_step)
    
    line_signal, = ax.plot(frame_time, np.zeros_like(frame_time), color='b', linestyle='-', 
                                    linewidth=1.5, 
                                    label='Moduliertes Signal (Modulated signal)')
    
    line_positive, = ax.plot(frame_time, np.zeros_like(frame_time), 
                                      color='r', linestyle='--', 
                                      linewidth=1, alpha=0.7, 
                                      label='Hüllkurve (Envelope) (+M(t))')
    
    line_negative, = ax.plot(frame_time, np.zeros_like(frame_time), 
                                      color='r', linestyle='--', 
                                      linewidth=1, alpha=0.7, 
                                      label='Hüllkurve (Envelope) (-M(t))')
    
    ax.legend(loc='upper right')
    
    
    def update(frame: int) -> tuple:
        start_time = frame * animation_step
        current_time = start_time + frame_time
        
        if modulation is None:
            M_t = np.ones_like(current_time)
        else:
            M_t = modulation(current_time)
        
        carrier = np.sin(2 * np.pi * fc * current_time)
        
        if modulation is None:
            s_t = carrier
        else:
            s_t = M_t * carrier
        
        line_signal.set_ydata(s_t)
        line_positive.set_ydata(M_t)
        line_negative.set_ydata(-M_t)
        
        ax.set_title('Amplitudenmoduliertes Signal\n(Amplitude-modulated signal)', fontsize=14)
        
        return (line_signal, line_positive, line_negative)
    
    anim = animation.FuncAnimation(
        fig,   
        update,   
        frames=num_frames,
        interval=20,
        blit=True,
        repeat=True
    )
    
    if save_path:
            anim.save(save_path, writer='pillow', fps=20)

    
    plt.show()
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