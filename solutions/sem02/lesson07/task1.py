from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:

    if diagram_type not in {"box", "violin", "hist"}:
        raise ValueError
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    space = 0.2
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

    axis_scatter.scatter(abscissa, ordinates, color="darkred", alpha=0.5)

    if diagram_type == "hist":
        axis_hor.hist(
            abscissa,
            bins=100,
            color="orange",
            density=True,
            alpha=0.5,
        )
        axis_vert.hist(
            ordinates,
            orientation="horizontal",
            bins=100,
            color="red",
            density=True,
            alpha=0.5,
        )

        axis_hor.invert_yaxis()
        axis_vert.invert_xaxis()

    elif diagram_type == "box":
        axis_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="yellow", color="orange"),
            medianprops=dict(color="red"),
        )
        axis_vert.boxplot(
            ordinates,
            patch_artist=True,
            boxprops=dict(facecolor="yellow", color="orange"),
            medianprops=dict(color="red"),
        )

        axis_hor.invert_yaxis()
        axis_vert.invert_xaxis()

    else:
        v_hor = axis_hor.violinplot(abscissa, vert=False)
        v_vert = axis_vert.violinplot(ordinates, vert=True)

        for v in [v_hor, v_vert]:
            for body in v["bodies"]:
                body.set_facecolor("red")
                body.set_edgecolor("darkred")
                body.set_alpha(0.5)

        for v in [v_hor, v_vert]:
            for part in v:
                if part == "bodies":
                    continue

                v[part].set_edgecolor("red")

    axis_hor.invert_yaxis()
    axis_vert.invert_xaxis()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    plt.style.use("ggplot")
    visualize_diagrams(abscissa, ordinates, "hist")

    plt.savefig("plot.png")
    # plt.show()
