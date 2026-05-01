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

    allcolor = "red"
    plt.style.use("dark_background")

    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    if diagram_type not in ("hist", "violin", "box"):
        raise ValueError

    fig = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)

    ax_main = fig.add_subplot(grid[1:, :-1])
    ax_main.scatter(abscissa, ordinates, color=allcolor, alpha=0.5)

    ax_top = fig.add_subplot(grid[0, :-1], sharex=ax_main)
    ax_left = fig.add_subplot(grid[1:, -1], sharey=ax_main)

    if diagram_type == "hist":
        ax_top.hist(abscissa, bins=50, color=allcolor, density=True, alpha=0.5)
        ax_left.hist(
            ordinates, bins=50, color=allcolor, density=True, alpha=0.5, orientation="horizontal"
        )
    elif diagram_type == "violin":
        ax_top.violinplot(abscissa, vert=False)
        ax_left.violinplot(ordinates, vert=True)
    elif diagram_type == "box":
        ax_top.boxplot(abscissa, vert=False)
        ax_left.boxplot(ordinates, vert=True)

    ax_top.xaxis.set_visible(False)
    ax_left.yaxis.set_visible(False)


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T
    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
