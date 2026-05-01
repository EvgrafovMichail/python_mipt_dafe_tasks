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

    axis_scatter.scatter(abscissa, ordinates, color="cornflowerblue", alpha=0.5)

    if diagram_type == "hist":
        axis_hor.hist(
            abscissa,
            bins=50,
            color="cornflowerblue",
            density=True,
            alpha=0.5,
        )

        axis_vert.hist(
            ordinates,
            bins=50,
            color="cornflowerblue",
            orientation="horizontal",
            density=True,
            alpha=0.5,
        )

    if diagram_type == "violin":
        violin_parts_hor = axis_hor.violinplot(
            abscissa,
            orientation="horizontal",
        )

        violin_parts_vert = axis_vert.violinplot(
            ordinates,
        )

        for violin_parts in (violin_parts_hor, violin_parts_vert):
            for body in violin_parts["bodies"]:
                body.set_facecolor("cornflowerblue")
                body.set_edgecolor("blue")

            for part in violin_parts:
                if part == "bodies":
                    continue
                violin_parts[part].set_edgecolor("cornflowerblue")

    if diagram_type == "box":
        axis_hor.boxplot(
            abscissa,
            orientation="horizontal",
            patch_artist=True,
            boxprops=dict(facecolor="lightsteelblue"),
            medianprops=dict(color="k"),
        )

        axis_vert.boxplot(
            ordinates,
            patch_artist=True,
            boxprops=dict(facecolor="lightsteelblue"),
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
    plt.show()
