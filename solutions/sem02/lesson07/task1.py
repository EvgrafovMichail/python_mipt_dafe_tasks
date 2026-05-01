from typing import Any

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")


class ShapeMismatchError(Exception):
    pass


def _plot_dist(ax, data, dtype, vert):
    if dtype == "hist":
        ax.hist(
            data,
            bins=50,
            color="cornflowerblue",
            density=True,
            alpha=0.7,
            orientation="horizontal" if vert else "vertical",
        )
    elif dtype == "box":
        ax.boxplot(
            data,
            vert=vert,
            patch_artist=True,
            boxprops=dict(facecolor="lightsteelblue"),
            medianprops=dict(color="k"),
        )
    elif dtype == "violin":
        p = ax.violinplot(data, vert=vert, showmedians=True)
        for b in p["bodies"]:
            b.set_facecolor("cornflowerblue")
            b.set_edgecolor("blue")
        for k in p:
            if k != "bodies":
                p[k].set_edgecolor("cornflowerblue")


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError
    if diagram_type not in ("hist", "violin", "box"):
        raise ValueError

    fig = plt.figure(figsize=(8, 8))
    gs = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)

    ax1 = fig.add_subplot(gs[:-1, 1:])
    ax2 = fig.add_subplot(gs[:-1, 0], sharey=ax1)
    ax3 = fig.add_subplot(gs[-1, 1:], sharex=ax1)

    ax1.scatter(abscissa, ordinates, color="cornflowerblue", alpha=0.7)
    ax1.set_title("Диаграмма рассеяния", fontsize=14, color="dimgray")

    _plot_dist(ax3, abscissa, diagram_type, vert=False)
    _plot_dist(ax2, ordinates, diagram_type, vert=True)

    ax3.invert_yaxis()
    ax2.invert_xaxis()

    plt.savefig("task1.png")


if __name__ == "__main__":
    np.random.seed(42)
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T
    visualize_diagrams(abscissa, ordinates, "hist")
