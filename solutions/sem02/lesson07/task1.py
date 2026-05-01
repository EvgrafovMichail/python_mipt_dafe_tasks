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
        raise ShapeMismatchError("Размеры массивов не совпадают")

    if diagram_type not in ["hist", "violin", "box"]:
        raise ValueError("Недопустимое значение diagram_type")

    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_scatter.scatter(abscissa, ordinates, alpha=0.5)

    # график распределения по оси Y
    axis_vert = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)

    if diagram_type == "hist":
        axis_vert.hist(
            ordinates,
            bins=50,
            orientation="horizontal",
            alpha=0.5,
            color="red",
            density=True,
            edgecolor="black",
        )
    elif diagram_type == "violin":
        axis_vert.violinplot(ordinates, vert=True, showmedians=True)
        axis_vert.set_yticks([])
    else:
        axis_vert.boxplot(ordinates, vert=True, patch_artist=True)
        axis_vert.set_yticks([])

    # график распределения по оси X
    axis_hor = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)

    if diagram_type == "hist":
        axis_hor.hist(abscissa, bins=50, alpha=0.5, color="blue", density=True, edgecolor="black")
    elif diagram_type == "violin":
        axis_hor.violinplot(abscissa, vert=False, showmedians=True)
        axis_hor.set_xticks([])
    else:
        axis_hor.boxplot(abscissa, vert=False, patch_artist=True)
        axis_hor.set_xticks([])

    axis_hor.invert_yaxis()
    axis_vert.invert_xaxis()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
