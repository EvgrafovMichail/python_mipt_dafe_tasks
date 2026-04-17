import json
import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter


def _sample_times(window_sec, dt):
    return np.arange(0.0, window_sec, dt)


def _modulating_factor(envelope, t_absolute):
    if envelope is None:
        return 1.0
    return np.asarray(envelope(t_absolute))


def _rf_waveform(t_absolute, carrier_hz, envelope):
    gain = _modulating_factor(envelope, t_absolute)
    phase = 2.0 * np.pi * carrier_hz * t_absolute
    return gain * np.sin(phase)


def _prepare_axes(ax, plot_duration, has_envelope):
    ax.set_xlim(0.0, plot_duration)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("t (s)")
    ax.set_ylabel("s(t)")
    ax.set_title("AM signal" if has_envelope else "Carrier signal")


def _anim_init(line):
    line.set_data([], [])
    return (line,)


def _anim_frame(frame_idx, line, t_rel, carrier_hz, envelope, animation_step):
    t_abs = frame_idx * animation_step + t_rel
    y = _rf_waveform(t_abs, carrier_hz, envelope)
    line.set_data(t_rel, y)
    return (line,)


def _harmonic_envelope(tau, dc, amplitude, omega):
    return dc + amplitude * np.sin(omega * np.asarray(tau))


def create_animation(
    modulation,
    fc,
    num_frames,
    plot_duration,
    time_step=0.001,
    animation_step=0.01,
    save_path="",
):
    t_rel = _sample_times(plot_duration, time_step)
    fig, ax = plt.subplots()
    (line,) = ax.plot([], [], lw=1.5)
    _prepare_axes(ax, plot_duration, modulation is not None)

    interval_ms = int(max(1, round(animation_step * 1000)))
    animation = FuncAnimation(
        fig,
        lambda frame_idx, l=line, tr=t_rel, c=fc, e=modulation, s=animation_step: _anim_frame(
            frame_idx, l, tr, c, e, s
        ),
        init_func=lambda ln=line: _anim_init(ln),
        frames=num_frames,
        interval=interval_ms,
        blit=True,
    )

    fig._animation = animation

    if save_path:
        animation.save(save_path, writer=PillowWriter(fps=20))

    return animation


def load_config(config_path):
    base_dir = os.path.dirname(os.path.abspath(config_path))
    with open(config_path, encoding="utf-8") as f:
        d = json.load(f)
    mod = None
    if d.get("mod_omega") is not None:
        mod = lambda tau, dc=float(d["mod_dc"]), a=float(d["mod_amplitude"]), w=float(
            d["mod_omega"]
        ): _harmonic_envelope(tau, dc, a, w)
    save_path = d.get("save_path") or ""
    if save_path:
        save_path = os.path.abspath(os.path.join(base_dir, save_path))
    return {
        "modulation": mod,
        "fc": float(d["fc"]),
        "num_frames": int(d["num_frames"]),
        "plot_duration": float(d["plot_duration"]),
        "time_step": float(d["time_step"]),
        "animation_step": float(d["animation_step"]),
        "save_path": save_path,
    }


if __name__ == "__main__":
    cfg = os.path.join(os.path.dirname(os.path.abspath(__file__)), "animation_config.json")
    animation = create_animation(**load_config(cfg))
    plt.show()
