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
    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_hist_vert = figure.add_subplot(
        grid[:-1, 0],
        sharey=axis_scatter,
    )
    axis_hist_hor = figure.add_subplot(
        grid[-1, 1:],
        sharex=axis_scatter,
    )

    axis_scatter.scatter(abscissa, ordinates, color="mediumpurple", alpha=0.7)

    if diagram_type == "box":
        axis_hist_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="mediumpurple", alpha=0.7),
            medianprops=dict(color="black", linewidth=0.5),
        )
        axis_hist_vert.boxplot(
            ordinates,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor="mediumpurple", alpha=0.7),
            medianprops=dict(color="black", linewidth=0.5),
        )

        axis_hist_hor.set_yticks([])
        axis_hist_vert.set_xticks([])

    elif diagram_type == "hist":
        axis_hist_hor.hist(
            abscissa,
            bins=50,
            color="mediumpurple",
            density=True,
            alpha=0.7,
        )
        axis_hist_vert.hist(
            ordinates,
            bins=50,
            color="mediumpurple",
            orientation="horizontal",
            density=True,
            alpha=0.7,
        )

    elif diagram_type == "violin":
        vils = [None, None]
        vils[0] = axis_hist_hor.violinplot(abscissa, vert=False)
        vils[1] = axis_hist_vert.violinplot(ordinates, vert=True)

        for i in vils:
            for body in i["bodies"]:
                body.set_facecolor("red")
                body.set_edgecolor("brown")

            for part in i:
                if part == "bodies":
                    continue

                i[part].set_edgecolor("darkred")
                i[part].set_linewidth(0.5)

        axis_hist_hor.set_yticks([])
        axis_hist_vert.set_xticks([])

    else:
        raise ValueError("Unknown diagram type")

    axis_hist_hor.invert_yaxis()
    axis_hist_vert.invert_xaxis()

    plt.show()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
