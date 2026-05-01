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
        raise ShapeMismatchError("abscissa and ordinates must be of equal size")

    if diagram_type not in ("hist", "violin", "box"):
        raise ValueError("diagram_type must be one of: hist, violin, box")

    plt.style.use("ggplot")

    figure = plt.figure(figsize=(10, 10))
    grid = plt.GridSpec(4, 4, wspace=0.15, hspace=0.15)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_left = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)
    axis_bottom = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)

    axis_scatter.scatter(abscissa, ordinates, color="royalblue", alpha=0.55, s=30)
    axis_scatter.set_title(
        "Диаграмма рассеяния",
        fontsize=16,
        fontweight="bold",
        c="dimgray",
    )
    axis_scatter.set_xlabel("abscissa", fontsize=12, fontweight="bold", c="dimgray")
    axis_scatter.set_ylabel("ordinates", fontsize=12, fontweight="bold", c="dimgray")

    if diagram_type == "hist":
        axis_bottom.hist(
            abscissa,
            bins=30,
            color="cornflowerblue",
            edgecolor="blue",
            alpha=0.65,
        )
        axis_left.hist(
            ordinates,
            bins=30,
            color="sandybrown",
            edgecolor="chocolate",
            alpha=0.65,
            orientation="horizontal",
        )
        axis_bottom.invert_yaxis()
        axis_left.invert_xaxis()
    elif diagram_type == "box":
        axis_bottom.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="cornflowerblue"),
            medianprops=dict(color="navy"),
        )
        axis_left.boxplot(
            ordinates,
            patch_artist=True,
            boxprops=dict(facecolor="sandybrown"),
            medianprops=dict(color="maroon"),
        )
    else:
        violin_bottom = axis_bottom.violinplot(
            abscissa,
            vert=False,
            showmedians=True,
        )
        for body in violin_bottom["bodies"]:
            body.set_facecolor("cornflowerblue")
            body.set_edgecolor("blue")

        for part in violin_bottom:
            if part == "bodies":
                continue
            violin_bottom[part].set_edgecolor("cornflowerblue")

        violin_left = axis_left.violinplot(
            ordinates,
            showmedians=True,
        )
        for body in violin_left["bodies"]:
            body.set_facecolor("sandybrown")
            body.set_edgecolor("chocolate")

        for part in violin_left:
            if part == "bodies":
                continue
            violin_left[part].set_edgecolor("sandybrown")

    axis_left.tick_params(axis="y", labelleft=False)
    axis_bottom.tick_params(axis="x", labelbottom=False)

    plt.show()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
