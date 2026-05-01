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

    plt.style.use("seaborn-v0_8")

    if (abscissa.shape != ordinates.shape) or (abscissa.size != ordinates.size):
        raise ShapeMismatchError

    if diagram_type not in ("hist", "violin", "box"):
        raise ValueError

    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_hist_vert = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)
    axis_hist_hor = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)

    axis_scatter.scatter(abscissa, ordinates, c=ordinates, cmap="viridis", marker="H", alpha=0.5)

    if diagram_type == "hist":
        axis_hist_hor.hist(
            abscissa,
            bins=50,
            ensity=True,
            color="#95D5B2",
            edgecolor="#2D6A4F",
            linewidth=1.5,
            linestyle="-",
            alpha=0.6,
        )

        axis_hist_vert.hist(
            ordinates,
            bins=50,
            density=True,
            orientation="horizontal",
            color="#95D5B2",
            edgecolor="#2D6A4F",
            linewidth=1.5,
            linestyle="-",
            alpha=0.6,
        )

    elif diagram_type == "violin":
        v_hor = axis_hist_hor.violinplot(
            abscissa,
            positions=[1],
            vert=False,
            widths=0.7,
            showmeans=True,
            showmedians=True,
            showextrema=True,
            quantiles=[[0.25, 0.75]],
        )
        for body in v_hor["bodies"]:
            body.set(facecolor="#95D5B2", edgecolor="#2D6A4F", alpha=0.6, linewidth=1.5)
        for key, color in [
            ("cmaxes", "#2D6A4F"),
            ("cmins", "#2D6A4F"),
            ("cbars", "#2D6A4F"),
            ("cmedians", "#D62828"),
            ("cmeans", "#F9C74F"),
        ]:
            v_hor[key].set_color(color)

        v_vert = axis_hist_vert.violinplot(
            ordinates,
            positions=[1],
            vert=True,
            widths=0.7,
            showmeans=True,
            showmedians=True,
            showextrema=True,
        )
        for body in v_vert["bodies"]:
            body.set(facecolor="#52B788", edgecolor="#1B4332", alpha=0.6, linewidth=1.5)
        for key, color in [
            ("cmaxes", "#1B4332"),
            ("cmins", "#1B4332"),
            ("cbars", "#1B4332"),
            ("cmedians", "#D62828"),
            ("cmeans", "#F9C74F"),
        ]:
            v_vert[key].set_color(color)

    elif diagram_type == "box":
        axis_hist_hor.boxplot(
            abscissa,
            positions=[1],
            widths=0.6,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor="#95D5B2", edgecolor="#2D6A4F", linewidth=1.5),
            whiskerprops=dict(color="#2D6A4F", linewidth=1.5),
            capprops=dict(color="#2D6A4F", linewidth=1.5),
            medianprops=dict(color="#D62828", linewidth=2),
            meanprops=dict(
                marker="D", markerfacecolor="#F9C74F", markeredgecolor="#2D6A4F", markersize=8
            ),
            showmeans=True,
        )
        axis_hist_vert.boxplot(
            ordinates,
            positions=[1],
            widths=0.6,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor="#52B788", edgecolor="#1B4332", linewidth=1.5),
            whiskerprops=dict(color="#1B4332", linewidth=1.5),
            capprops=dict(color="#1B4332", linewidth=1.5),
            medianprops=dict(color="#D62828", linewidth=2),
            meanprops=dict(
                marker="D", markerfacecolor="#F9C74F", markeredgecolor="#1B4332", markersize=8
            ),
            showmeans=True,
        )

    axis_hist_hor.invert_yaxis()
    axis_hist_vert.invert_xaxis()

    for ax in [axis_scatter, axis_hist_hor, axis_hist_vert]:
        ax.grid(True, which="major", linestyle="--", linewidth=0.6, alpha=0.5, color="gray")
        ax.grid(True, which="minor", linestyle=":", linewidth=0.3, alpha=0.3)
        ax.minorticks_on()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "box")
    plt.show()
