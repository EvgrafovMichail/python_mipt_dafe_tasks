from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


def check(x: np.ndarray, y: np.ndarray, mode: Any) -> None:
    if x.shape != y.shape:
        raise ShapeMismatchError
    if mode not in {"hist", "violin", "box"}:
        raise ValueError


def layout():
    plt.style.use("ggplot")
    fig = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=0.25, hspace=0.25)

    main = fig.add_subplot(grid[:-1, 1:])
    x_ax = fig.add_subplot(grid[-1, 1:], sharex=main)
    y_ax = fig.add_subplot(grid[:-1, 0], sharey=main)

    return main, x_ax, y_ax


def scatter(ax, x, y):
    ax.scatter(x, y, s=12, alpha=0.6, color="darkcyan")


def hist(x_ax, y_ax, x, y):
    x_ax.hist(x, bins=40, color="darkcyan", alpha=0.4, density=True)
    y_ax.hist(y, bins=40, orientation="horizontal", color="darkcyan", alpha=0.4, density=True)


def violin(x_ax, y_ax, x, y):
    vx = x_ax.violinplot(x, vert=False, showmedians=True)
    vy = y_ax.violinplot(y, vert=True, showmedians=True)

    for b in vx["bodies"]:
        b.set_facecolor("teal")
        b.set_alpha(0.5)

    for b in vy["bodies"]:
        b.set_facecolor("teal")
        b.set_alpha(0.5)


def box(x_ax, y_ax, x, y):
    x_ax.boxplot(
        x,
        vert=False,
        patch_artist=True,
        boxprops=dict(facecolor="teal"),
        medianprops=dict(color="black"),
    )
    y_ax.boxplot(
        y,
        vert=True,
        patch_artist=True,
        boxprops=dict(facecolor="teal"),
        medianprops=dict(color="black"),
    )


def visualize_diagrams(x: np.ndarray, y: np.ndarray, mode: Any) -> None:
    check(x, y, mode)

    main, x_ax, y_ax = layout()
    scatter(main, x, y)

    if mode == "hist":
        hist(x_ax, y_ax, x, y)
    elif mode == "violin":
        violin(x_ax, y_ax, x, y)
    elif mode == "box":
        box(x_ax, y_ax, x, y)

    x_ax.invert_yaxis()
    y_ax.invert_xaxis()

    plt.show()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]

    x, y = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(x, y, "hist")
