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

    valid_types = {"hist", "violin", "box"}
    if diagram_type not in valid_types:
        raise ValueError

    figure = plt.figure(figsize=(10, 10))
    grid = plt.GridSpec(4, 4, wspace=0.3, hspace=0.3)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])

    axis_left = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)

    axis_bottom = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)

    scatter_color = "#6A5ACD"
    dist_color = "#87CEEB"
    edge_color = "#4169E1"

    axis_scatter.scatter(
        abscissa, ordinates, color=scatter_color, alpha=0.6, edgecolors="white", linewidth=0.5, s=50
    )
    axis_scatter.set_xlabel("Абциссы", fontsize=11, fontweight="bold")
    axis_scatter.set_ylabel("Ординаты", fontsize=11, fontweight="bold")
    axis_scatter.set_title("Точечный график", fontsize=14, fontweight="bold", pad=15)
    axis_scatter.grid(True, alpha=0.3, linestyle="--")

    if diagram_type == "hist":
        axis_bottom.hist(
            abscissa, bins=40, color=dist_color, edgecolor=edge_color, alpha=0.7, density=True
        )
        axis_bottom.set_ylabel("Плотность", fontsize=10)

    elif diagram_type == "violin":
        violin_parts = axis_bottom.violinplot(
            abscissa, vert=False, showmedians=True, showmeans=False, showextrema=True
        )

        for body in violin_parts["bodies"]:
            body.set_facecolor(dist_color)
            body.set_edgecolor(edge_color)
            body.set_alpha(0.7)

        for part_name in ("cbars", "cmins", "cmaxes", "cmedians"):
            if part_name in violin_parts:
                violin_parts[part_name].set_edgecolor(edge_color)
                violin_parts[part_name].set_linewidth(1.5)
        axis_bottom.set_ylabel("Violin", fontsize=10)

    else:
        axis_bottom.boxplot(
            abscissa,
            vert=False,
            patch_artist=True,
            boxprops=dict(facecolor=dist_color, edgecolor=edge_color, alpha=0.7),
            whiskerprops=dict(color=edge_color, linewidth=1.5),
            capprops=dict(color=edge_color, linewidth=1.5),
            medianprops=dict(color="darkblue", linewidth=2),
            flierprops=dict(
                marker="o", markerfacecolor=dist_color, markeredgecolor=edge_color, alpha=0.5
            ),
        )
        axis_bottom.set_ylabel("Box", fontsize=10)

    axis_bottom.set_xlabel("Распределение по оси абцисс", fontsize=12, fontweight="bold")
    axis_bottom.grid(True, alpha=0.3, linestyle="--", axis="x")

    if diagram_type == "hist":
        axis_left.hist(
            ordinates,
            bins=40,
            color=dist_color,
            edgecolor=edge_color,
            alpha=0.7,
            density=True,
            orientation="horizontal",
        )
        axis_left.set_xlabel("Плотность", fontsize=10)

    elif diagram_type == "violin":
        violin_parts = axis_left.violinplot(
            ordinates, vert=True, showmedians=True, showmeans=False, showextrema=True
        )

        for body in violin_parts["bodies"]:
            body.set_facecolor(dist_color)
            body.set_edgecolor(edge_color)
            body.set_alpha(0.7)

        for part_name in ("cbars", "cmins", "cmaxes", "cmedians"):
            if part_name in violin_parts:
                violin_parts[part_name].set_edgecolor(edge_color)
                violin_parts[part_name].set_linewidth(1.5)
        axis_left.set_xlabel("Violin", fontsize=10)

    else:
        axis_left.boxplot(
            ordinates,
            vert=True,
            patch_artist=True,
            boxprops=dict(facecolor=dist_color, edgecolor=edge_color, alpha=0.7),
            whiskerprops=dict(color=edge_color, linewidth=1.5),
            capprops=dict(color=edge_color, linewidth=1.5),
            medianprops=dict(color="darkblue", linewidth=2),
            flierprops=dict(
                marker="o", markerfacecolor=dist_color, markeredgecolor=edge_color, alpha=0.5
            ),
        )
        axis_left.set_xlabel("Box", fontsize=10)

    axis_left.set_ylabel("Распределение по оси ординат", fontsize=12, fontweight="bold")
    axis_left.grid(True, alpha=0.3, linestyle="--", axis="x")

    axis_bottom.invert_yaxis()
    axis_left.invert_xaxis()

    figure.suptitle(
        f"Визуализация распределения данных\nТип распределения: {diagram_type.capitalize()}",
        fontsize=16,
        fontweight="bold",
        y=1.02,
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "box")
    plt.show()
