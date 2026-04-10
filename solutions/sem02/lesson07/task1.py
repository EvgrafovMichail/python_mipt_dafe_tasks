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
    fig = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)
    scat_graph = fig.add_subplot(grid[0:-1, 1:])
    graph1 = fig.add_subplot(grid[0:-1, 0], sharey=scat_graph)
    graph2 = fig.add_subplot(grid[-1, 1:], sharex=scat_graph)
    scat_graph.scatter(abscissa, ordinates, color="#00FF00", alpha=0.3)

    if diagram_type == "box":
        graph1.boxplot(
            ordinates,
            boxprops={"color": "#00FF00"},
        )
        graph2.boxplot(
            abscissa,
            vert=False,
            boxprops={"color": "#00FF00"},
        )

    if diagram_type == "violin":
        viol_vertical = graph1.violinplot(
            ordinates,
            showmedians=True,
        )
        for body in viol_vertical["bodies"]:
            body.set_facecolor("#00FF00")
            body.set_edgecolor("black")
        for parts in viol_vertical:
            if parts == "bodies":
                continue
            viol_vertical[parts].set_edgecolor("black")

        viol_horizontal = graph2.violinplot(abscissa, vert=False, showmedians=True)
        for body in viol_horizontal["bodies"]:
            body.set_facecolor("#00FF00")
            body.set_edgecolor("black")
        for parts in viol_horizontal:
            if parts == "bodies":
                continue
            viol_horizontal[parts].set_edgecolor("black")
    
    if diagram_type == "hist":
        graph1.hist(
            ordinates, orientation="horizontal", bins=50, color="#00FF00", alpha=0.3, edgecolor="black"
        )
        graph2.hist(abscissa, bins=50, color="#00FF00", alpha=0.3, edgecolor="black")
        graph1.invert_xaxis()
        graph2.invert_yaxis()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
