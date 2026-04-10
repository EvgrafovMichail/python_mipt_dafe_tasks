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
    if abscissa.size != ordinates.size:
        raise ShapeMismatchError
    if diagram_type not in ("hist", "violin", "box"):
        raise ValueError

    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_hist_vert = figure.add_subplot(
        grid[:-1, 0],
        sharey=axis_scatter,
    )
    axis_hist_hor = figure.add_subplot(
        grid[-1, 1:],
        sharex=axis_scatter,
    )

    if diagram_type == "hist":
        axis_scatter.scatter(abscissa, ordinates, color="green", alpha=0.5)
        axis_hist_hor.hist(
            abscissa,
            bins=50,
            color="green",
            density=True,
            alpha=0.5,
        )
        axis_hist_vert.hist(
            ordinates,
            bins=50,
            color="green",
            orientation="horizontal",
            density=True,
            alpha=0.5,
        )
        axis_hist_hor.invert_yaxis()
        axis_hist_vert.invert_xaxis()

    elif diagram_type == "violin":
        axis_scatter.scatter(abscissa, ordinates, color="green", alpha=0.5)
        hist_hor = axis_hist_hor.violinplot(abscissa, vert=False)
        hist_vert = axis_hist_vert.violinplot(ordinates, vert=True)

        for body in hist_vert["bodies"]:
            body.set_facecolor("green")
            body.set_edgecolor("black")
        for parts in hist_vert:
            if parts == "bodies":
                continue
            hist_vert[parts].set_edgecolor("black")
        for body in hist_hor["bodies"]:
            body.set_facecolor("green")
            body.set_edgecolor("black")
        for parts in hist_hor:
            if parts == "bodies":
                continue
            hist_hor[parts].set_edgecolor("black")

    elif diagram_type == "box":
        axis_scatter.scatter(abscissa, ordinates, color="green", alpha=0.5)
        axis_hist_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="lightgreen"),
            medianprops=dict(color="k"),
        )
        axis_hist_vert.boxplot(
            ordinates,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor="lightgreen"),
            medianprops=dict(color="k"),
        )


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "box")
    plt.show()
