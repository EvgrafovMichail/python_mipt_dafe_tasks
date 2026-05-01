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
    correct_type = {"hist", "violin", "box"}
    if diagram_type not in correct_type:
        raise ValueError
    fig = plt.figure(figsize=(10, 10))
    grid = plt.GridSpec(4, 4, wspace=0.2, hspace=0.2)
    ax_scatter = fig.add_subplot(grid[:-1, 1:])
    ax_vert = fig.add_subplot(grid[:-1, 0], sharey=ax_scatter)
    ax_hor = fig.add_subplot(grid[-1, 1:], sharex=ax_scatter)
    ax_scatter.scatter(abscissa, ordinates, color="cornflowerblue", alpha=0.5, s=20)
    ax_scatter.set_xlabel("Ось X")
    ax_scatter.set_ylabel("Ось Y")

    if diagram_type == "hist":
        ax_hor.hist(abscissa, bins=50, color="cornflowerblue", density=True, alpha=0.5)
        ax_vert.hist(
            ordinates,
            bins=50,
            color="cornflowerblue",
            density=True,
            orientation="horizontal",
            alpha=0.5,
        )
        ax_hor.invert_yaxis()
        ax_vert.invert_xaxis()
    elif diagram_type == "violin":
        vp_hor = ax_hor.violinplot(abscissa, vert=False, showmedians=True, positions=[0])
        vp_vert = ax_vert.violinplot(ordinates, vert=True, showmedians=True, positions=[0])
        for vp in (vp_hor, vp_vert):
            for body in vp["bodies"]:
                body.set_facecolor("cornflowerblue")
                body.set_edgecolor("blue")
            for part in vp:
                if part == "bodies":
                    continue
                vp[part].set_edgecolor("cornflowerblue")
        ax_hor.set_ylim(-0.5, 0.5)
        ax_vert.set_xlim(-0.5, 0.5)
    elif diagram_type == "box":
        ax_hor.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            positions=[0],
            boxprops=dict(facecolor="lightsteelblue"),
            medianprops=dict(color="k"),
        )
        ax_vert.boxplot(
            ordinates,
            vert=True,
            patch_artist=True,
            positions=[0],
            boxprops=dict(facecolor="lightsteelblue"),
            medianprops=dict(color="k"),
        )
        ax_hor.set_ylim(-0.5, 0.5)
        ax_vert.set_xlim(-0.5, 0.5)

    ax_hor.set_ylabel("")
    ax_hor.tick_params(axis="y", left=False, labelleft=False)
    ax_vert.set_xlabel("")
    ax_vert.tick_params(axis="x", bottom=False, labelbottom=False)

    plt.tight_layout()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
