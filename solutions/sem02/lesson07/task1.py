from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


def validate(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if len(abscissa) != len(ordinates):
        raise ShapeMismatchError()
    if diagram_type not in {"hist", "violin", "box"}:
        raise ValueError()


def create_axes() -> tuple[plt.Figure, plt.Axes, plt.Axes, plt.Axes]:
    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)
    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_hist_vert = figure.add_subplot(
        grid[:-1, 0],
        sharey=axis_scatter,
    )
    axis_hist_hor = figure.add_subplot(
        grid[-1, 1:],
        sharex=axis_scatter,
    )
    return figure, axis_scatter, axis_hist_vert, axis_hist_hor


def draw_marginal(
    ax: plt.Axes,
    data: np.ndarray,
    diagram_type: str,
    orientation: str,
) -> None:
    if diagram_type == "hist":
        if orientation == "horizontal":
            ax.hist(
                data,
                bins=50,
                color="cornflowerblue",
                density=True,
                alpha=0.5,
                orientation="horizontal",
            )
        else:
            ax.hist(
                data,
                bins=50,
                color="cornflowerblue",
                density=True,
                alpha=0.5,
            )
    elif diagram_type == "violin":
        vert = orientation == "vertical"
        vp = ax.violinplot(data, vert=vert, showmedians=True)
        for body in vp["bodies"]:
            body.set_facecolor("cornflowerblue")
            body.set_edgecolor("blue")
        for part in vp:
            if part != "bodies":
                vp[part].set_edgecolor("cornflowerblue")
    else:
        vert = orientation == "vertical"
        ax.boxplot(
            data,
            vert=vert,
            patch_artist=True,
            boxprops={"facecolor": "lightsteelblue"},
            medianprops={"color": "k"},
        )


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    validate(abscissa, ordinates, diagram_type)
    fig, ax_scatter, ax_left, ax_bottom = create_axes()

    ax_scatter.scatter(abscissa, ordinates, color="cornflowerblue", alpha=0.5)

    draw_marginal(ax_bottom, abscissa, diagram_type, "vertical")
    draw_marginal(ax_left, ordinates, diagram_type, "horizontal")

    ax_bottom.invert_yaxis()
    ax_left.invert_xaxis()
    ax_left.tick_params(labelleft=False, labelbottom=False)
    ax_bottom.tick_params(labelleft=False, labelbottom=False)


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
