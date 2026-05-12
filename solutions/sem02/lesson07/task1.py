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
    if diagram_type not in {"box", "violin", "hist"}:
        raise ValueError
    grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)
    figure = plt.figure(figsize=(8, 8))
    scatter = figure.add_subplot(grid[:-1, 1:])
    abs = figure.add_subplot(grid[:-1, 0], sharex=scatter)
    ord = figure.add_subplot(grid[-1, 1:], sharey=scatter)
    scatter.scatter(abscissa, ordinates, color="green", alpha=0.5)
    if diagram_type == "box":
        ord.boxplot(
            ordinates,
            patch_artist=True,
            boxprops=dict(facecolor="red", color="lightgreen"),
            medianprops=dict(color="black"),
        )
        abs.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="red", color="lightgreen"),
            medianprops=dict(color="black"),
        )
        abs.invert_yaxis()
        ord.invert_xaxis()
    elif diagram_type == "hist":
        ord.hist(abscissa, bins=100, color="lightgreen", density=True, alpha=0.5)
        abs.hist(
            ordinates,
            orientation="horizontal",
            bins=100,
            color="lightgreen",
            density=True,
            alpha=0.5,
        )
        ord.invert_xaxis()
        abs.invert_yaxis()
    else:
        vert = ord.violinplot(ordinates, showmedians=True)
        hor = abs.violinplot(abscissa, showmedians=True, vert=False)
        for v in [hor, vert]:
            for body in v["bodies"]:
                body.set_facecolor("lightgreen")
                body.set_edgecolor("green")
                body.set_alpha(0.5)
            for i in v:
                if i == "bodies":
                    continue
                v[i].set_edgecolor("lightgreen")
        abs.invert_yaxis()
        ord.invert_xaxis()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
