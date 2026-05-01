from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


def draw_hist(
    abscissa: np.ndarray, ordinates: np.ndarray, axis_hor: plt.Axes, axis_vert: plt.Axes
) -> None:
    axis_hor.hist(
        abscissa,
        bins=50,
        color="#6093db",
        density=True,
        alpha=0.75,
    )

    axis_vert.hist(
        ordinates,
        bins=50,
        color="#6093db",
        orientation="horizontal",
        density=True,
        alpha=0.75,
    )

    axis_hor.invert_yaxis()
    axis_vert.invert_xaxis()


def draw_violin(
    abscissa: np.ndarray, ordinates: np.ndarray, axis_hor: plt.Axes, axis_vert: plt.Axes
) -> None:
    axis_hor.violinplot(
        abscissa,
        vert=False,
        showmedians=True,
    )

    axis_vert.violinplot(
        ordinates,
        vert=True,
        showmedians=True,
    )


def draw_box(
    abscissa: np.ndarray, ordinates: np.ndarray, axis_hor: plt.Axes, axis_vert: plt.Axes
) -> None:
    axis_hor.boxplot(
        abscissa,
        vert=False,
        patch_artist=True,
        boxprops=dict(facecolor="#d5bd8c"),
        medianprops=dict(color="k"),
    )
    axis_hor.set_yticks([])

    axis_vert.boxplot(
        ordinates,
        vert=True,
        patch_artist=True,
        boxprops=dict(facecolor="#d5bd8c"),
        medianprops=dict(color="k"),
    )
    axis_vert.set_xticks([])


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape[0] != ordinates.shape[0]:
        raise ShapeMismatchError
    if diagram_type not in ["hist", "violin", "box"]:
        raise ValueError(
            f"Expected 'hist', 'violin' or 'box' as diagram_type, got '{diagram_type}' instead"
        )

    plt.style.use("fivethirtyeight")
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

    axis_scatter.scatter(abscissa, ordinates, color="#7655ea", alpha=0.5)

    if diagram_type == "hist":
        draw_hist(abscissa, ordinates, axis_hor, axis_vert)
    elif diagram_type == "violin":
        draw_violin(abscissa, ordinates, axis_hor, axis_vert)
    elif diagram_type == "box":
        draw_box(abscissa, ordinates, axis_hor, axis_vert)

    plt.show()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
