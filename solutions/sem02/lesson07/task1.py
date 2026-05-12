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

    if not (diagram_type == "hist" or diagram_type == "violin" or diagram_type == "box"):
        raise ValueError

    space = 0.2

    figure = plt.figure(figsize=(8, 8))
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

    axis_scatter.scatter(abscissa, ordinates, color="deeppink", alpha=0.3)

    if diagram_type == "hist":
        axis_hor.hist(
            abscissa,
            bins=50,
            color="lightpink",
            density=True,
            alpha=0.5,
            edgecolor="palevioletred",
            linewidth=1,
        )

        axis_vert.hist(
            ordinates,
            bins=50,
            color="lightpink",
            orientation="horizontal",
            density=True,
            alpha=0.5,
            edgecolor="palevioletred",
            linewidth=1,
        )

        axis_hor.invert_yaxis()
        axis_vert.invert_xaxis()

    if diagram_type == "violin":
        violin_hor = axis_hor.violinplot(
            abscissa,
            vert=False,
            showmedians=True,
        )

        for body in violin_hor["bodies"]:
            body.set_facecolor("violet")
            body.set_edgecolor("darkmagenta")
            body.set_linewidth(2)

        for part in violin_hor:
            if part == "bodies":
                continue

            violin_hor[part].set_edgecolor("darkmagenta")

        violin_vert = axis_vert.violinplot(
            ordinates,
            vert=True,
            showmedians=True,
        )

        for body in violin_vert["bodies"]:
            body.set_facecolor("violet")
            body.set_edgecolor("darkmagenta")
            body.set_linewidth(2)

        for part in violin_vert:
            if part == "bodies":
                continue

            violin_vert[part].set_edgecolor("darkmagenta")

    if diagram_type == "box":
        axis_hor.boxplot(
            ordinates,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="lightcoral"),
            medianprops=dict(color="firebrick"),
        )
        axis_vert.set_xticks([])
        axis_vert.set_xlabel("y values")

        axis_vert.boxplot(
            abscissa,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor="lightcoral"),
            medianprops=dict(color="firebrick"),
        )
        axis_hor.set_yticks([])
        axis_hor.set_xlabel("x values")


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    visualize_diagrams(abscissa, ordinates, "violin")
    visualize_diagrams(abscissa, ordinates, "box")

    plt.show()
