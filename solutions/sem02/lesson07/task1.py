from typing import Any, Callable

import matplotlib.pyplot as plt
import numpy as np

PRIMARY_COLOR = "#FF1493"
SECONDARY_COLOR = "#C71585"
SPACE = 0.2


class ShapeMismatchError(Exception):
    pass


def change_color_violin(violin_parts):
    for vp in violin_parts:
        plt.setp(vp["bodies"], facecolor=SECONDARY_COLOR, edgecolor=PRIMARY_COLOR)

        line_keys = set(vp.keys()) - {"bodies"}
        for key in line_keys:
            plt.setp(vp[key], edgecolor=SECONDARY_COLOR)


def draw_hists(axis_hist_hor, axis_hist_vert, abscissa, ordinates, color=PRIMARY_COLOR):
    axis_hist_hor.hist(abscissa, bins=50, color=color, alpha=0.5, density=True)
    axis_hist_vert.hist(
        ordinates, bins=50, color=color, alpha=0.5, density=True, orientation="horizontal"
    )


def draw_boxes(axis_hist_hor, axis_hist_vert, abscissa, ordinates, color=SECONDARY_COLOR):
    props = dict(
        patch_artist=True,
        boxprops=dict(facecolor=color, color=color),
        medianprops=dict(color=PRIMARY_COLOR),
    )
    axis_hist_hor.boxplot(abscissa, vert=False, **props)
    axis_hist_vert.boxplot(ordinates, **props)


def draw_violins(axis_hist_hor, axis_hist_vert, abscissa, ordinates):
    v_parts = [
        axis_hist_hor.violinplot(abscissa, vert=False, showmedians=True),
        axis_hist_vert.violinplot(ordinates, showmedians=True),
    ]
    change_color_violin(v_parts)


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    drawers: dict[str, Callable] = {"hist": draw_hists, "box": draw_boxes, "violin": draw_violins}

    if diagram_type not in drawers:
        raise ValueError

    figure = plt.figure(figsize=(8, 8))
    grid = plt.GridSpec(4, 4, wspace=SPACE, hspace=SPACE)

    axis_scatter = figure.add_subplot(grid[:-1, 1:])
    axis_hist_vert = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)
    axis_hist_hor = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)

    axis_scatter.scatter(abscissa, ordinates, color=PRIMARY_COLOR, alpha=0.4, s=15)
    drawers[diagram_type](axis_hist_hor, axis_hist_vert, abscissa, ordinates)

    axis_hist_hor.invert_yaxis()
    axis_hist_vert.invert_xaxis()
    axis_hist_hor.set_yticks([])
    axis_hist_vert.set_xticks([])

    plt.show()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "violin")
    # plt.show()
