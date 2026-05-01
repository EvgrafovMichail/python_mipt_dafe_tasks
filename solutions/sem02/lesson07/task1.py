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
    plt.style.use("ggplot")
    if diagram_type == "hist":
        bins_amount = abscissa.size // 20
        figure = plt.figure(figsize=(9, 9))
        grid = plt.GridSpec(4, 4)

        axis_scatter = figure.add_subplot(grid[:-1, 1:])
        axis_hist_vert = figure.add_subplot(
            grid[:-1, 0],
            sharey=axis_scatter,
        )
        axis_hist_hor = figure.add_subplot(
            grid[-1, 1:],
            sharex=axis_scatter,
        )

        axis_scatter.scatter(abscissa, ordinates, color="purple", alpha=0.5)
        axis_hist_hor.hist(
            abscissa,
            bins=bins_amount,
            color="cornflowerblue",
            edgecolor="blue",
            density=True,
            alpha=0.7,
        )
        axis_hist_vert.hist(
            ordinates,
            bins=bins_amount,
            color="indianred",
            edgecolor="red",
            orientation="horizontal",
            density=True,
            alpha=0.7,
        )

        axis_hist_hor.invert_yaxis()
        axis_hist_vert.invert_xaxis()
    elif diagram_type == "box":
        figure = plt.figure(figsize=(9, 9))
        grid = plt.GridSpec(4, 4)

        axis_scatter = figure.add_subplot(grid[:-1, 1:])
        axis_box_vert = figure.add_subplot(
            grid[:-1, 0],
            sharey=axis_scatter,
        )
        axis_box_hor = figure.add_subplot(
            grid[-1, 1:],
            sharex=axis_scatter,
        )

        axis_scatter.scatter(abscissa, ordinates, color="cornflowerblue", alpha=0.5)
        axis_box_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="lightsteelblue"),
            medianprops=dict(color="k"),
        )
        axis_box_vert.boxplot(
            ordinates,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor="lightsteelblue"),
            medianprops=dict(color="k"),
        )
        axis_box_hor.invert_yaxis()
        axis_box_vert.invert_xaxis()
    elif diagram_type == "violin":
        figure = plt.figure(figsize=(9, 9))
        grid = plt.GridSpec(4, 4)

        axis_scatter = figure.add_subplot(grid[:-1, 1:])
        axis_viol_vert = figure.add_subplot(
            grid[:-1, 0],
            sharey=axis_scatter,
        )
        axis_viol_hor = figure.add_subplot(
            grid[-1, 1:],
            sharex=axis_scatter,
        )

        axis_scatter.scatter(abscissa, ordinates, color="purple", alpha=0.5)
        parts_hor = axis_viol_hor.violinplot(
            abscissa,
            vert=False,
            showmedians=True,
        )
        for body in parts_hor["bodies"]:
            body.set_facecolor("cornflowerblue")
            body.set_edgecolor("blue")

        for part in parts_hor:
            if part == "bodies":
                continue
            parts_hor[part].set_edgecolor("cornflowerblue")

        parts_viol = axis_viol_vert.violinplot(
            ordinates,
            vert=True,
            showmedians=True,
        )
        for body in parts_viol["bodies"]:
            body.set_facecolor("indianred")
            body.set_edgecolor("red")

        for part in parts_viol:
            if part == "bodies":
                continue
            parts_viol[part].set_edgecolor("indianred")
        axis_viol_hor.invert_yaxis()
        axis_viol_vert.invert_xaxis()
    else:
        raise ValueError


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
