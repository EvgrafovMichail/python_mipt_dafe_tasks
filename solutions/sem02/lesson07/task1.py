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

    axis_scatter.scatter(abscissa, ordinates, color="mediumseagreen", alpha=0.35)
    axis_scatter.set_title("Distribution", fontsize=17, fontweight="bold", c="dimgray")

    if diagram_type == "hist":
        axis_hor.hist(
            abscissa,
            bins=50,
            color="aquamarine",
            density=True,
            alpha=0.7,
        )
        axis_vert.hist(
            ordinates,
            bins=50,
            color="aquamarine",
            orientation="horizontal",
            density=True,
            alpha=0.7,
        )
        axis_hor.invert_yaxis()
        axis_vert.invert_xaxis()

    elif diagram_type == "violin":
        violin_parts_vert = axis_vert.violinplot(abscissa, vert=True, showmedians=True)
        violin_parts_hor = axis_hor.violinplot(ordinates, vert=False, showmedians=True)
        for body in violin_parts_vert["bodies"]:
            body.set_facecolor("mediumseagreen")
            body.set_edgecolor("aquamarine")

        for part in violin_parts_vert:
            if part == "bodies":
                continue

            violin_parts_vert[part].set_edgecolor("mediumseagreen")

        for body in violin_parts_hor["bodies"]:
            body.set_facecolor("mediumseagreen")
            body.set_edgecolor("aquamarine")

        for part in violin_parts_hor:
            if part == "bodies":
                continue

            violin_parts_hor[part].set_edgecolor("mediumseagreen")

    elif diagram_type == "box":
        axis_vert.boxplot(
            abscissa,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor="mediumseagreen", alpha=0.7),
        )
        axis_hor.boxplot(
            ordinates,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="mediumseagreen", alpha=0.7),
        )

    axis_vert.set_ylabel("Vertical", fontsize=17, fontweight="bold", c="dimgray")
    axis_hor.set_xlabel("Horizontal", fontsize=17, fontweight="bold", c="dimgray")


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
