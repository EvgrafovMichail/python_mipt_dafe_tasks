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
    if abscissa.shape[0] != ordinates.shape[0] or diagram_type not in ["hist", "box", "violin"]:
        raise ShapeMismatchError
    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)
    scat_graph = figure.add_subplot(grid[0:-1, 1:])
    ord_vert_graph = figure.add_subplot(grid[0:-1, 0], sharey=scat_graph)
    abs_hor_graph = figure.add_subplot(grid[-1, 1:], sharex=scat_graph)
    scat_graph.scatter(abscissa, ordinates, color="red", alpha=0.5)
    if diagram_type == "box":
        ord_vert_graph.boxplot(
            ordinates,
            patch_artist=True,
            boxprops={"facecolor": "red", "linewidth": 2},
            medianprops={"color": "black"},
        )
        abs_hor_graph.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops={"facecolor": "red", "linewidth": 2},
            medianprops={"color": "black"},
        )
    if diagram_type == "hist":
        ord_vert_graph.hist(
            ordinates, orientation="horizontal", bins=50, color="red", alpha=0.5, edgecolor="black"
        )
        abs_hor_graph.hist(abscissa, bins=50, color="red", alpha=0.5, edgecolor="black")
        ord_vert_graph.invert_xaxis()
        abs_hor_graph.invert_yaxis()

    if diagram_type == "violin":
        viol_vert = ord_vert_graph.violinplot(
            ordinates,
            showmedians=True,
        )
        for body in viol_vert["bodies"]:
            body.set_facecolor("red")
            body.set_edgecolor("black")
        for parts in viol_vert:
            if parts == "bodies":
                continue
            viol_vert[parts].set_edgecolor("black")
        viol_hor = abs_hor_graph.violinplot(abscissa, vert=False, showmedians=True)
        for body in viol_hor["bodies"]:
            body.set_facecolor("red")
            body.set_edgecolor("black")
        for parts in viol_hor:
            if parts == "bodies":
                continue
            viol_hor[parts].set_edgecolor("black")


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
