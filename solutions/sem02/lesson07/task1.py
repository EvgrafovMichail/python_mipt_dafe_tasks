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
    if abscissa.shape[0] != ordinates.shape[0]:
        raise ShapeMismatchError
    
    if diagram_type not in ["hist", "box", "violin"]:
        raise ValueError

    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    axis_scatter = figure.add_subplot(grid[0:-1, 1:])
    axis_hist_vert = figure.add_subplot(grid[0:-1, 0], sharey=axis_scatter)
    axis_hist_hor = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)

    axis_scatter.scatter(abscissa, ordinates, color="cornflowerblue", alpha=0.5)

    if diagram_type == "box":
        axis_hist_vert.boxplot(
            ordinates,
            patch_artist=True,
            boxprops={"facecolor": "lightsteelblue"},
            medianprops={"color": "black"},
        )
        axis_hist_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops={"facecolor": "lightsteelblue"},
            medianprops={"color": "black"},
        )

    elif diagram_type == "hist":
        axis_hist_vert.hist(
            ordinates,
            orientation="horizontal",
            bins=50,
            color="cornflowerblue",
            alpha=0.5,
            density=True,
        )
        axis_hist_hor.hist(
            abscissa,
            bins=50,
            color="cornflowerblue",
            alpha=0.5,
            density=True,
        )
        axis_hist_vert.invert_xaxis()
        axis_hist_hor.invert_yaxis()

    elif diagram_type == "violin":
        viol_vert = axis_hist_vert.violinplot(ordinates, showmedians=True)
        for body in viol_vert["bodies"]:
            body.set_facecolor("cornflowerblue")
            body.set_edgecolor("blue")
        for part in viol_vert:
            if part != "bodies":
                viol_vert[part].set_edgecolor("cornflowerblue")

        viol_hor = axis_hist_hor.violinplot(abscissa, vert=False, showmedians=True)
        for body in viol_hor["bodies"]:
            body.set_facecolor("cornflowerblue")
            body.set_edgecolor("blue")
        for part in viol_hor:
            if part != "bodies":
                viol_hor[part].set_edgecolor("cornflowerblue")

    axis_hist_hor.set_yticks([])
    axis_hist_vert.set_xticks([])

    plt.show()



if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "box")
    plt.show()
