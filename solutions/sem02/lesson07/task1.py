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

    if diagram_type not in {"hist", "violin", "box"}:
        raise ValueError

    space = 0.2
    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_vert = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)
    axis_hor = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)

    axis_scatter.scatter(abscissa, ordinates, color="mediumpurple", alpha=0.5)

    if diagram_type == "hist":
        axis_hor.hist(
            abscissa,
            bins=50,
            color="mediumpurple",
            density=True,
            alpha=0.5,
        )
        axis_vert.hist(
            ordinates,
            bins=50,
            color="mediumpurple",
            orientation="horizontal",
            density=True,
            alpha=0.5,
        )

        axis_hor.invert_yaxis()
        axis_vert.invert_xaxis()

    elif diagram_type == "violin":
        parts_hor = axis_hor.violinplot(abscissa, vert=False, showmedians=True)
        parts_vert = axis_vert.violinplot(ordinates, vert=True, showmedians=True)
        for parts in (parts_hor, parts_vert):
            for body in parts["bodies"]:
                body.set_facecolor("cornflowerblue")
                body.set_edgecolor("blue")
            for key in parts:
                if key != "bodies":
                    parts[key].set_edgecolor("cornflowerblue")
        axis_hor.set_yticks([])
        axis_vert.set_xticks([])

    elif diagram_type == "box":
        box_props = dict(facecolor="lightsteelblue")
        median_props = dict(color="k")
        axis_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=box_props,
            medianprops=median_props,
        )
        axis_vert.boxplot(
            ordinates,
            vert=True,
            patch_artist=True,
            boxprops=box_props,
            medianprops=median_props,
        )
        axis_hor.set_yticks([])
        axis_vert.set_xticks([])

    plt.show()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
