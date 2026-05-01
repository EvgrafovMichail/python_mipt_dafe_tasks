from typing import Any

import matplotlib.gridspec as gridspec
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
    if diagram_type not in ("hist", "violin", "box"):
        raise ValueError

    fig = plt.figure(figsize=(10, 10), facecolor="#cfd3cd")

    gs = gridspec.GridSpec(
        2,
        2,
        width_ratios=[1, 4],
        height_ratios=[4, 1],
        hspace=0.1,
        wspace=0.1,
        left=0.08,
        right=0.98,
        top=0.98,
        bottom=0.08,
    )

    ax_scatter = fig.add_subplot(gs[0, 1])
    ax_diag_x = fig.add_subplot(gs[1, 1])
    ax_diag_y = fig.add_subplot(gs[0, 0])
    ax_diag_x.grid(True)
    ax_diag_y.grid(True)
    ax_scatter.grid(True)
    ax_scatter.tick_params(labelsize=16)
    ax_diag_x.tick_params(labelsize=16)
    ax_diag_y.tick_params(labelsize=16)

    ax_scatter.scatter(abscissa, ordinates, alpha=0.5, marker="o", s=100, color="sandybrown")

    if diagram_type == "hist":
        ax_diag_x.hist(
            abscissa, bins=30, color="cornflowerblue", edgecolor="dimgray", alpha=0.7, density=True
        )
        ax_diag_y.hist(
            ordinates,
            bins=30,
            orientation="horizontal",
            color="cornflowerblue",
            edgecolor="dimgray",
            alpha=0.7,
            density=True,
        )

    elif diagram_type == "violin":
        ax_diag_x.violinplot(abscissa, vert=False)
        ax_diag_y.violinplot(ordinates, vert=True)

    elif diagram_type == "box":
        ax_diag_x.boxplot(abscissa, vert=False)
        ax_diag_y.boxplot(ordinates, vert=True)

    ax_diag_x.invert_yaxis()
    ax_diag_y.invert_xaxis()

    plt.savefig("scatter_with_diagrams.png")

    pass


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
