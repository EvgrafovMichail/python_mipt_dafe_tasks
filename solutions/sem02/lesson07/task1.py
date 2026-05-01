from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


data = np.random.normal(0, 1, 1000)


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError
    if diagram_type != "hist" and diagram_type != "violin" and diagram_type != "box":
        raise ValueError

    fig, axes = plt.subplots(2, 1, figsize=(16, 9))

    if diagram_type == "hist":
        axes[0].hist(abscissa, bins=50, color="mistyrose", edgecolor="mediumpurple")
        axes[1].hist(ordinates, bins=50, color="mistyrose", edgecolor="mediumpurple")

    elif diagram_type == "violin":
        violin_parts_0 = axes[0].violinplot([abscissa], vert=False, showmedians=True)
        violin_parts_1 = axes[1].violinplot([ordinates], vert=False, showmedians=True)
        for violin_parts in [violin_parts_0, violin_parts_1]:
            for body in violin_parts["bodies"]:
                body.set_facecolor("mistyrose")
                body.set_edgecolor("mediumpurple")
            for part in violin_parts:
                if part == "bodies":
                    continue
                violin_parts[part].set_edgecolor("cornflowerblue")
        axes[0].set_yticks([])
        axes[1].set_yticks([])
    elif diagram_type == "box":
        axes[0].boxplot(
            abscissa,
            vert=False,
            boxprops=dict(facecolor="mistyrose"),
            patch_artist=True,
            medianprops=dict(color="purple"),
        )
        axes[1].boxplot(
            ordinates,
            vert=False,
            boxprops=dict(facecolor="mistyrose"),
            patch_artist=True,
            medianprops=dict(color="purple"),
        )

    pass


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
