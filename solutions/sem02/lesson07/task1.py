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

    plt.style.use("ggplot")
    figure = plt.figure(figsize=(12, 10))
    grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_y = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)
    axis_x = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)

    axis_scatter.scatter(abscissa, ordinates, color="cornflowerblue", alpha=0.5)

    match diagram_type:

        case "hist":
            axis_x.hist(abscissa, bins = 112, alpha = 0.5, color = 'b')
            axis_y.hist(ordinates, orientation="horizontal", bins = 112, alpha = 0.5, color = 'b')

        case "box":
            axis_x.boxplot(abscissa, orientation = "horizontal")
            axis_y.boxplot(ordinates)

        case "violin":
            axis_x.violinplot(abscissa, orientation="horizontal")
            axis_y.violinplot(ordinates)

        case _:
            raise ValueError


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "violin")
    plt.show()
print("done")
