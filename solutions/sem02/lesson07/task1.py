from typing import Any

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")


class ShapeMismatchError(Exception):
    pass


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.size != ordinates.size:
        raise ShapeMismatchError

    figure = plt.figure(figsize=(8, 8))
    gs = plt.GridSpec(2, 2, width_ratios=[1, 3], height_ratios=[3, 1])
    ord_ax = figure.add_subplot(gs[0, 0])
    abs_ax = figure.add_subplot(gs[1, 1])
    scat_ax = figure.add_subplot(gs[0, 1])

    match diagram_type:
        case "hist":
            ord_ax.hist(
                ordinates,
                bins=50,
                color="#0090B4",
                edgecolor="#86CFFF",
                density=True,
                label="ordinates",
                alpha=0.3,
                orientation="horizontal",
            )
            abs_ax.hist(
                abscissa,
                bins=50,
                color="#0090B4",
                edgecolor="#86CFFF",
                density=True,
                label="abscissa",
                alpha=0.3,
                orientation="vertical",
            )

            ord_ax.invert_xaxis()
            abs_ax.invert_yaxis()
            ord_ax.legend(loc="lower left")
            abs_ax.legend(loc="lower right")

        case "violin":

            def set_colors(violin_parts) -> None:
                for body in violin_parts["bodies"]:
                    body.set_facecolor("#0090B4")
                    body.set_edgecolor("#86CFFF")

                for part in violin_parts:
                    if part != "bodies":
                        violin_parts[part].set_edgecolor("#86CFFF")

            violin_parts = ord_ax.violinplot(
                ordinates,
                vert=True,
                showmedians=True,
            )
            set_colors(violin_parts)

            violin_parts = abs_ax.violinplot(
                abscissa,
                vert=False,
                showmedians=True,
            )
            set_colors(violin_parts)

        case "box":
            ord_ax.boxplot(
                ordinates,
                vert=True,
                patch_artist=True,
                boxprops=dict(facecolor="#0090B4", alpha=0.3),
                medianprops=dict(color="#86CFFF"),
            )
            abs_ax.boxplot(
                abscissa,
                vert=False,
                patch_artist=True,
                boxprops=dict(facecolor="#0090B4", alpha=0.3),
                medianprops=dict(color="#86CFFF"),
            )

        case _:
            raise ValueError

    scat_ax.scatter(abscissa, ordinates, color="#0090B4", edgecolors="#86CFFF", alpha=0.3)


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    visualize_diagrams(abscissa, ordinates, "violin")
    visualize_diagrams(abscissa, ordinates, "box")
    plt.show()
