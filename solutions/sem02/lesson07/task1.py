from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    valid_types = {"hist", "violin", "box"}
    if diagram_type not in valid_types:
        raise ValueError

    fig = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)

    ax_scat = fig.add_subplot(grid[:-1, 1:])
    ax_v = fig.add_subplot(grid[:-1, 0], sharey=ax_scat)
    ax_h = fig.add_subplot(grid[-1, 1:], sharex=ax_scat)

    ax_scat.scatter(abscissa, ordinates, color="steelblue", alpha=0.35)
    ax_scat.set_title("Distribution", fontsize=17, fontweight="bold", c="black")

    if diagram_type == "hist":
        hist_params = {
            "bins": 50,
            "color": "steelblue",
            "edgecolor": "navy",
            "alpha": 0.7,
            "density": True,
        }
        ax_h.hist(abscissa, **hist_params)
        ax_v.hist(ordinates, orientation="horizontal", **hist_params)
        ax_h.invert_yaxis()
        ax_v.invert_xaxis()

    elif diagram_type == "violin":

        def set_violin(axis, data, vertical):
            parts = axis.violinplot(data, vert=vertical, showmedians=True)
            for body in parts["bodies"]:
                body.set_facecolor("steelblue")
                body.set_edgecolor("lightsteelblue")
            for part in parts:
                if part == "bodies":
                    continue
                parts[part].set_edgecolor("steelblue")

        set_violin(ax_h, ordinates, vertical=False)
        set_violin(ax_v, abscissa, vertical=True)

    elif diagram_type == "box":
        box_props = {"facecolor": "steelblue", "alpha": 0.7}
        box_params = {"patch_artist": True, "boxprops": box_props}
        ax_v.boxplot(abscissa, vert=True, **box_params)
        ax_h.boxplot(ordinates, vert=False, **box_params)

    ax_v.set_ylabel("Vertical", fontsize=17, fontweight="bold", c="dimgray")
    ax_h.set_xlabel("Horizontal", fontsize=17, fontweight="bold", c="dimgray")


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
