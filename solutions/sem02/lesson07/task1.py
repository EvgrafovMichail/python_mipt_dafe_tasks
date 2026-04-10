from typing import Any

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")


class ShapeMismatchError(Exception):
    pass


def apply_custom_style(ax):
    ax.set_facecolor("#F0F0F0")
    ax.grid(True, color="#6E6E6E", linestyle="-", linewidth=0.5)
    ax.set_axisbelow(True)


def draw_hist(fig, grid, labels, colors):
    ax = fig.add_subplot(grid[:-1, 1:])
    apply_custom_style(ax)
    ax.hist(abscissa, bins=50, alpha=0.5, label=labels[0], color=colors[0])
    ax.hist(ordinates, bins=50, alpha=0.5, label=labels[1], color=colors[1])
    ax.set_title("Гистограмма")
    ax.legend()


def draw_violin(fig, grid, labels, colors):
    ax = fig.add_subplot(grid[:-1, 0])
    apply_custom_style(ax)
    violin_parts = ax.violinplot([abscissa, ordinates], vert=True, showmedians=True)

    for i, body in enumerate(violin_parts["bodies"]):
        body.set_facecolor(colors[i])
        body.set_edgecolor(colors[i])
        body.set_alpha(0.6)

    for part_name in violin_parts:
        if part_name != "bodies":
            violin_parts[part_name].set_edgecolor("black")
            violin_parts[part_name].set_linewidth(1.5)

    violin_parts["cmedians"].set_linewidth(2.5)
    ax.set_xticks([1, 2])
    ax.set_xticklabels(labels)
    ax.set_title("Скрипичная диаграмма")


def draw_box(fig, grid, labels, colors):
    ax = fig.add_subplot(grid[-1, 1:])
    apply_custom_style(ax)
    box_parts = ax.boxplot(
        [abscissa, ordinates], labels=labels, vert=False, patch_artist=True, notch=True
    )

    for patch, color in zip(box_parts["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax.set_title("Ящик с усами")


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    if diagram_type not in ["hist", "violin", "box", "all"]:
        raise ValueError

    colors = ["#0A29C2", "#EAC90F"]
    labels = ["X data", "Y data"]
    space = 0.4

    fig = plt.figure(figsize=(12, 10))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=2 * space, height_ratios=[1, 1, 1, 1.5])

    types_to_draw = ["hist", "violin", "box"] if diagram_type == "all" else [diagram_type]

    for d_type in types_to_draw:
        if d_type == "hist":
            draw_hist(fig, grid, labels, colors)

        if d_type == "violin":
            draw_violin(fig, grid, labels, colors)

        if d_type == "box":
            draw_box(fig, grid, labels, colors)


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "all")
    plt.show()
