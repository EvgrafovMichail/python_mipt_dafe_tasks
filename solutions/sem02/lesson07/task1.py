from typing import Any, Final

import matplotlib.pyplot as plt
import numpy as np

ALLOWED_DIAGRAM_TYPES: Final = frozenset(
    [
        "hist",
        "box",
        "violin",
    ]
)


class ColorConfig:
    scatter: Final[dict] = {
        "color": "#7FA6B5",
        "edgecolors": "#647075",
        "alpha": 0.6,
    }

    hist: Final[dict] = {
        "color": "#BFAB95",
        "edgecolor": "#4B4033",
        "alpha": 0.7,
    }

    box: Final[dict] = {
        "boxprops": {"facecolor": "#BFAB95", "edgecolor": "#4B4033", "alpha": 0.8},
        "medianprops": {
            "color": "#4B4033",
        },
    }

    violin: Final[str] = "#BFAB95"
    violin_edge: Final[str] = "#4B4033"


class ShapeMismatchError(Exception):
    pass


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if diagram_type not in ALLOWED_DIAGRAM_TYPES:
        raise ValueError

    if abscissa.size != ordinates.size:
        raise ShapeMismatchError

    figure = plt.figure(figsize=(16, 9))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    scatter = figure.add_subplot(grid[:-1, 1:])
    vert_axis = figure.add_subplot(grid[:-1, 0], sharey=scatter)
    hor_axis = figure.add_subplot(grid[-1, 1:], sharex=scatter)

    scatter.scatter(abscissa, ordinates, s=70, **ColorConfig.scatter)
    match diagram_type:
        case "hist":
            vert_axis.hist(
                ordinates,
                bins=70,
                orientation="horizontal",
                **ColorConfig.hist,
            )
            hor_axis.hist(
                abscissa,
                bins=70,
                **ColorConfig.hist,
            )

        case "box":
            vert_axis.boxplot(ordinates, vert=True, **ColorConfig.box)
            hor_axis.boxplot(abscissa, vert=False, **ColorConfig.box)

        case "violin":
            vert_violin = vert_axis.violinplot(ordinates, showmedians=True, vert=True)
            hor_violin = hor_axis.violinplot(abscissa, showmedians=True, vert=False)

            for body in vert_violin["bodies"]:
                body.set_facecolor(ColorConfig.violin)
                body.set_edgecolor(ColorConfig.violin_edge)

            for body in hor_violin["bodies"]:
                body.set_facecolor(ColorConfig.violin)
                body.set_edgecolor(ColorConfig.violin_edge)

    hor_axis.invert_yaxis()
    vert_axis.invert_xaxis()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "violin")
    plt.show()
