from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


def make_figure_axis(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    space: float = 0.2,
) -> tuple[plt.Figure, plt.Axes, plt.Axes, plt.Axes]:
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

    axis_scatter.scatter(
        abscissa,
        ordinates,
        color="mediumseagreen",
        alpha=0.35,
    )
    axis_scatter.set_title(
        "Distribution",
        fontsize=17,
        fontweight="bold",
        c="black",
    )

    return figure, axis_scatter, axis_hor, axis_vert


def create_hist_distribution(
    axis_hor: plt.Axes,
    axis_vert: plt.Axes,
    abscissa: np.ndarray,
    ordinates: np.ndarray,
) -> None:
    hist_params = {
        "bins": 50,
        "color": "mediumseagreen",
        "edgecolor": "darkgreen",
        "alpha": 0.7,
        "density": True,
    }

    axis_hor.hist(abscissa, **hist_params)
    axis_vert.hist(ordinates, orientation="horizontal", **hist_params)

    axis_hor.invert_yaxis()
    axis_vert.invert_xaxis()


def set_violin(
    axis: plt.Axes,
    data: np.ndarray,
    vertical: bool,
) -> None:
    violin_parts = axis.violinplot(data, vert=vertical, showmedians=True)

    for body in violin_parts["bodies"]:
        body.set_facecolor("mediumseagreen")
        body.set_edgecolor("aquamarine")

    for part in violin_parts:
        if part == "bodies":
            continue
        violin_parts[part].set_edgecolor("mediumseagreen")


def create_violin_distribution(
    axis_hor: plt.Axes,
    axis_vert: plt.Axes,
    abscissa: np.ndarray,
    ordinates: np.ndarray,
) -> None:
    set_violin(axis_hor, ordinates, vertical=False)
    set_violin(axis_vert, abscissa, vertical=True)


def create_box_distribution(
    axis_hor: plt.Axes,
    axis_vert: plt.Axes,
    abscissa: np.ndarray,
    ordinates: np.ndarray,
) -> None:
    box_props = {"facecolor": "mediumseagreen", "alpha": 0.7}
    box_params = {
        "patch_artist": True,
        "boxprops": box_props,
    }

    axis_vert.boxplot(abscissa, vert=True, **box_params)
    axis_hor.boxplot(ordinates, vert=False, **box_params)


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    valid_types = {"hist", "violin", "box"}
    if diagram_type not in valid_types:
        raise ValueError

    space = 0.2
    fig, ax_scatter, ax_hor, ax_vert = make_figure_axis(
        abscissa,
        ordinates,
        space,
    )

    if diagram_type == "hist":
        create_hist_distribution(ax_hor, ax_vert, abscissa, ordinates)
    elif diagram_type == "violin":
        create_violin_distribution(ax_hor, ax_vert, abscissa, ordinates)
    elif diagram_type == "box":
        create_box_distribution(ax_hor, ax_vert, abscissa, ordinates)

    ax_vert.set_ylabel(
        "Vertical",
        fontsize=17,
        fontweight="bold",
        c="dimgray",
    )
    ax_hor.set_xlabel(
        "Horizontal",
        fontsize=17,
        fontweight="bold",
        c="dimgray",
    )


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
