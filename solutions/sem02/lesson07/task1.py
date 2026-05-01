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
        raise ShapeMismatchError("Размеры массивов должны совпадать")

    allowed_types = ["hist", "violin", "box"]
    if diagram_type not in allowed_types:
        raise ValueError("Неверный diagram_type")

    fig = plt.figure(figsize=(10, 10))
    gs = fig.add_gridspec(2, 2, width_ratios=(1, 4), height_ratios=(4, 1), wspace=0.05, hspace=0.05)

    ax_scatter = fig.add_subplot(gs[0, 1])
    ax_dist_y = fig.add_subplot(gs[0, 0], sharey=ax_scatter)
    ax_dist_x = fig.add_subplot(gs[1, 1], sharex=ax_scatter)

    ax_scatter.scatter(abscissa, ordinates, alpha=0.6, color="red", s=20)
    ax_scatter.set_xlabel("Abscissa")
    ax_scatter.set_ylabel("Ordinates")

    if diagram_type == "violin":
        ax_dist_x.violinplot(abscissa, vert=False, showmedians=True)
        ax_dist_y.violinplot(ordinates, vert=True, showmedians=True)

    elif diagram_type == "hist":
        ax_dist_x.hist(abscissa, bins=30, color="red", alpha=0.4)
        ax_dist_y.hist(ordinates, bins=30, color="red", alpha=0.4, orientation="horizontal")

    elif diagram_type == "box":
        ax_dist_x.boxplot(abscissa, vert=False)
        ax_dist_y.boxplot(ordinates, vert=True)

    ax_dist_x.invert_yaxis()
    ax_dist_y.invert_xaxis()

    ax_dist_x.set_yticks([])
    ax_dist_y.set_xticks([])


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=100).T

    visualize_diagrams(abscissa, ordinates, "box")
    plt.show()
