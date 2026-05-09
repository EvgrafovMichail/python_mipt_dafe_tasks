from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    """Исключение, выбрасываемое при несовпадении размеров массивов."""

    pass


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    allowed_types = {"hist", "violin", "box"}
    if diagram_type not in allowed_types:
        raise ValueError

    main_color = "mediumseagreen"
    edge_color = "seagreen"

    figure = plt.figure(figsize=(9, 9))
    grid = plt.GridSpec(4, 4, wspace=0.3, hspace=0.3)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_dist_x = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)
    axis_dist_y = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)

    axis_dist_x.tick_params(axis="x", labelbottom=False)
    axis_dist_y.tick_params(axis="y", labelleft=False)

    axis_scatter.scatter(abscissa, ordinates, color=main_color, alpha=0.5, edgecolor=edge_color)

    if diagram_type == "hist":
        axis_dist_x.hist(
            abscissa, bins=40, color=main_color, edgecolor=edge_color, density=True, alpha=0.7
        )
        axis_dist_y.hist(
            ordinates,
            bins=40,
            color=main_color,
            edgecolor=edge_color,
            density=True,
            alpha=0.7,
            orientation="horizontal",
        )
        axis_dist_x.invert_yaxis()
        axis_dist_y.invert_xaxis()

    elif diagram_type == "box":
        axis_dist_x.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor=main_color, color=edge_color),
            medianprops=dict(color="k"),
        )
        axis_dist_y.boxplot(
            ordinates,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor=main_color, color=edge_color),
            medianprops=dict(color="k"),
        )

        axis_dist_x.axis("off")
        axis_dist_y.axis("off")

    elif diagram_type == "violin":
        v_x = axis_dist_x.violinplot(abscissa, vert=False, showmedians=True)
        v_y = axis_dist_y.violinplot(ordinates, vert=True, showmedians=True)

        for parts in [v_x, v_y]:
            for body in parts["bodies"]:
                body.set_facecolor(main_color)
                body.set_edgecolor(edge_color)
                body.set_alpha(0.7)
            parts["cmedians"].set_color("k")
            parts["cmins"].set_color(edge_color)
            parts["cmaxes"].set_color(edge_color)
            parts["cbars"].set_color(edge_color)

        axis_dist_x.axis("off")
        axis_dist_y.axis("off")


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "violin")

    plt.show()
