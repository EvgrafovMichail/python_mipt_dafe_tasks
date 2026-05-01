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
        raise ShapeMismatchError("shapes do not match")
    if diagram_type not in ("hist", "box", "violin"):
        raise ValueError("invalid diagram type")

    figure = plt.figure(figsize=(8, 8))
    space = 0.3
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_scatter.scatter(abscissa, ordinates, color="cornflowerblue", alpha=0.5)

    if diagram_type == "hist":
        axis_vert = figure.add_subplot(
            grid[:-1, 0],
            sharey=axis_scatter,
        )
        axis_hor = figure.add_subplot(
            grid[-1, 1:],
            sharex=axis_scatter,
        )
        axis_hor.hist(
            abscissa,
            bins=50,
            color="red",
            density=True,
            alpha=0.5,
        )
        axis_vert.hist(
            ordinates,
            bins=50,
            color="grey",
            orientation="horizontal",
            density=True,
            alpha=0.5,
        )
        axis_hor.invert_yaxis()
        axis_vert.invert_xaxis()

    if diagram_type == "violin":
        axis_vert = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)
        violin_parts_vert = axis_vert.violinplot(ordinates, vert=True, showmedians=True)
        for body in violin_parts_vert["bodies"]:
            body.set_facecolor("grey")
            body.set_edgecolor("darkgrey")

        for part in violin_parts_vert:
            if part == "bodies":
                continue

            violin_parts_vert[part].set_edgecolor("grey")

        axis_hor = figure.add_subplot(
            grid[-1, 1:],
            sharex=axis_scatter,
        )
        violin_parts_hor = axis_hor.violinplot(abscissa, vert=False, showmedians=True)
        for body in violin_parts_hor["bodies"]:
            body.set_facecolor("red")
            body.set_edgecolor("orange")

        for part in violin_parts_hor:
            if part == "bodies":
                continue

            violin_parts_hor[part].set_edgecolor("red")

    if diagram_type == "box":
        axis_vert = figure.add_subplot(
            grid[:-1, 0],
            sharey=axis_scatter,
        )
        axis_vert.boxplot(
            ordinates,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor="grey"),
            medianprops=dict(color="black"),
        )
        axis_hor = figure.add_subplot(
            grid[-1, 1:],
            sharex=axis_scatter,
        )
        axis_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="red"),
            medianprops=dict(color="yellow"),
        )


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "violin")
    plt.show()
