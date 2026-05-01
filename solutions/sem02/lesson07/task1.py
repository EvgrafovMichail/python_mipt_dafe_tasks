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
    if diagram_type not in ["hist", "violin", "box"]:
        raise ValueError
    plt.style.use("seaborn-v0_8-darkgrid")
    space = 0.2
    figure = plt.figure(figsize=(10, 10))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)
    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_vert = figure.add_subplot(
        grid[:-1, 0],
        sharey=axis_scatter,
    )
    axis_hor = figure.add_subplot(
        grid[-1, 1:],
        sharex=axis_scatter,
    )
    axis_scatter.scatter(abscissa, ordinates, color="green", alpha=0.5)

    if diagram_type == "hist":
        axis_hor.hist(
            abscissa,
            bins=50,
            color="green",
            density=True,
            alpha=0.5,
        )
        axis_vert.hist(
            ordinates,
            bins=50,
            color="green",
            orientation="horizontal",
            density=True,
            alpha=0.5,
        )

        axis_hor.invert_yaxis()
        axis_vert.invert_xaxis()

    if diagram_type == "violin":
        axis_hor.violinplot(
            abscissa,
            vert=False,
            showmedians=True,
        )

        axis_vert.violinplot(
            ordinates,
            vert=True,
            showmedians=True,
        )
        axis_hor.invert_yaxis()
        axis_vert.invert_xaxis()

    if diagram_type == "box":
        axis_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="green"),
            medianprops=dict(color="k"),
        )

        axis_vert.boxplot(
            abscissa,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor="green"),
            medianprops=dict(color="k"),
        )
        axis_hor.invert_yaxis()
        axis_vert.invert_xaxis()

    plt.show()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
