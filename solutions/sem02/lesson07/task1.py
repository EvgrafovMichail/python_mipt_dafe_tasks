from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


def _validate_data(abscissa: np.ndarray, ordinates: np.ndarray, diagram_type: Any):
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    if diagram_type not in {"hist", "violin", "box"}:
        raise ValueError


def _draw_marginal(ax: plt.Axes, data: np.ndarray, diagram_type: str, orientation: str):
    color = "dodgerblue"
    alpha = 0.5
    is_vert = orientation == "vertical"

    if diagram_type == "hist":
        ax.hist(
            data,
            bins=30,
            orientation="horizontal" if not is_vert else "vertical",
            color=color,
            alpha=alpha,
            edgecolor="white",
            linewidth=0.5,
        )
    elif diagram_type == "violin":
        vp = ax.violinplot(data, vert=is_vert, showextrema=False)
        for body in vp["bodies"]:
            body.set_facecolor(color)
            body.set_alpha(alpha)
    elif diagram_type == "box":
        ax.boxplot(
            data,
            vert=is_vert,
            patch_artist=True,
            boxprops=dict(facecolor=color, alpha=alpha, color="slategray"),
            medianprops=dict(color="firebrick"),
        )


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    _validate_data(abscissa, ordinates, diagram_type)

    fig = plt.figure(figsize=(10, 10))
    gs = fig.add_gridspec(2, 2, width_ratios=(1, 4), height_ratios=(4, 1), wspace=0.12, hspace=0.12)

    ax_main = fig.add_subplot(gs[0, 1])
    ax_left = fig.add_subplot(gs[0, 0], sharey=ax_main)
    ax_bottom = fig.add_subplot(gs[1, 1], sharex=ax_main)

    ax_main.scatter(abscissa, ordinates, color="slategray", alpha=0.4, s=25, edgecolor="none")
    ax_main.grid(True, linestyle=":", alpha=0.6)
    ax_main.set_title(f"Distribution Analysis [{diagram_type}]", pad=20, fontsize=14, loc="right")

    _draw_marginal(ax_left, ordinates, diagram_type, orientation="horizontal")
    _draw_marginal(ax_bottom, abscissa, diagram_type, orientation="vertical")

    ax_left.invert_xaxis()
    ax_bottom.invert_yaxis()

    plt.setp(ax_main.get_yticklabels(), visible=False)
    plt.setp(ax_main.get_xticklabels(), visible=False)

    xticks_left = ax_left.get_xticks()
    if len(xticks_left) > 0:
        ax_left.set_xticks(xticks_left[:-1])

    yticks_bottom = ax_bottom.get_yticks()
    if len(yticks_bottom) > 0:
        ax_bottom.set_yticks(yticks_bottom[:-1])

    ax_bottom.set_xlabel("Abscissa (X)", fontsize=10, fontweight="bold")
    ax_left.set_ylabel("Ordinates (Y)", fontsize=10, fontweight="bold")

    plt.show()


if __name__ == "__main__":
    mean, cov = [2, 3], [[1, 1], [1, 2]]
    x, y = np.random.multivariate_normal(mean, cov, size=1000).T
    visualize_diagrams(x, y, "hist")
