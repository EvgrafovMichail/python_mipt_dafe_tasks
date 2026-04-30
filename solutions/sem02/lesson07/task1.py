# %%
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")


class ShapeMismatchError(Exception):
    pass


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    if diagram_type not in ["hist", "violin", "box"]:
        raise ValueError

    colors = ["#69b3a2", "#404080"]
    labels = ["X data", "Y data"]

    fig, ax = plt.subplots(figsize=(10, 6))

    if diagram_type == "hist":
        ax.hist(abscissa, bins=50, alpha=0.5, label=labels[0], color=colors[0])
        ax.hist(ordinates, bins=50, alpha=0.5, label=labels[1], color=colors[1])
        ax.set_title("Гистограмма распределений")

    if diagram_type == "violin":
        if diagram_type == "violin":
            violin_parts = ax.violinplot([abscissa, ordinates], vert=False, showmedians=True)

            for i, body in enumerate(violin_parts["bodies"]):
                body.set_facecolor(colors[i])
                body.set_edgecolor(colors[i])
                body.set_alpha(0.6)

            for part_name in violin_parts:
                if part_name != "bodies":
                    violin_parts[part_name].set_edgecolor(colors)
                    violin_parts[part_name].set_linewidth(1.5)

            violin_parts["cmedians"].set_linewidth(2.5)

            ax.set_yticks([1, 2])
            ax.set_yticklabels(labels)
            ax.set_title("Плотность распределения")

    if diagram_type == "box":
        box_parts = ax.boxplot(
            [abscissa, ordinates], labels=labels, vert=False, patch_artist=True, notch=True
        )

        for patch, color in zip(box_parts["boxes"], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        ax.set_title("Анализ выбросов")


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    visualize_diagrams(abscissa, ordinates, "violin")
    visualize_diagrams(abscissa, ordinates, "box")
    plt.show()
# %%
