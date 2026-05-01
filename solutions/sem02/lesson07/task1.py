from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


def set_style_for_violin(violin_parts_hor, violin_parts_vert):
    for body in violin_parts_hor["bodies"]:
        body.set_facecolor("lightpink")
        body.set_edgecolor("hotpink")

    for body in violin_parts_vert["bodies"]:
        body.set_facecolor("lightpink")
        body.set_edgecolor("hotpink")

    for part in violin_parts_hor:
        if part == "bodies":
            continue

        violin_parts_hor[part].set_edgecolor("hotpink")

    for part in violin_parts_vert:
        if part == "bodies":
            continue

        violin_parts_vert[part].set_edgecolor("hotpink")


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.size != ordinates.size:
        raise ShapeMismatchError
    if diagram_type != "hist" and diagram_type != "violin" and diagram_type != "box":
        raise ValueError

    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    axis_scatter = figure.add_subplot(grid[:-1, :-1])
    axis_diagram_vert = figure.add_subplot(
        grid[:-1, 3],
        sharey=axis_scatter,
    )
    axis_diagram_hor = figure.add_subplot(
        grid[-1, :-1],
        sharex=axis_scatter,
    )

    axis_scatter.scatter(abscissa, ordinates, color="hotpink", alpha=0.45)

    if diagram_type == "hist":
        axis_diagram_hor.hist(
            abscissa,
            bins=52,
            color="lightpink",
            density=True,
            alpha=0.8,
        )
        axis_diagram_vert.hist(
            ordinates,
            bins=52,
            color="lightpink",
            orientation="horizontal",
            density=True,
            alpha=0.8,
        )

    if diagram_type == "violin":
        violin_parts_hor = axis_diagram_hor.violinplot(abscissa, vert=False, showmedians=True)
        violin_parts_vert = axis_diagram_vert.violinplot(ordinates, showmedians=True)

        set_style_for_violin(violin_parts_hor, violin_parts_vert)

    if diagram_type == "box":
        axis_diagram_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="lightpink"),
            medianprops=dict(color="k"),
        )
        axis_diagram_vert.boxplot(
            ordinates,
            patch_artist=True,
            boxprops=dict(facecolor="lightpink"),
            medianprops=dict(color="k"),
        )

    axis_diagram_hor.invert_yaxis()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")

    plt.show()
