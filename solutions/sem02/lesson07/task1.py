from typing import Any

import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


class DiagramVisualizer:
    def __init__(self, abscissa: np.ndarray, ordinates: np.ndarray, space: float = 0.2) -> None:
        self._abscissa = abscissa
        self._ordinates = ordinates
        self._space = space
        self._validate()

    def _validate(self) -> None:
        if self._abscissa.shape != self._ordinates.shape:
            raise ShapeMismatchError

    def _setup_figure_grid_axes(self):
        figure = plt.figure(figsize=(8, 8))
        grid = plt.GridSpec(4, 4, wspace=self._space, hspace=self._space)

        axis_scatter = figure.add_subplot(grid[:-1, 1:])
        axis_horis = figure.add_subplot(grid[-1, 1:], sharex=axis_scatter)
        axis_vert = figure.add_subplot(grid[:-1, 0], sharey=axis_scatter)

        axis_horis.set_xlabel("Horizontal", fontsize=14, c="dimgray")
        axis_vert.set_ylabel("Vertical", fontsize=14, c="dimgray")

        return axis_scatter, axis_horis, axis_vert

    def _setup_scatter(self, axis_scatter: plt.Axes) -> None:
        axis_scatter.scatter(self._abscissa, self._ordinates, color="mediumseagreen", alpha=0.3)
        axis_scatter.set_title("Distribution", fontsize=17, fontweight="bold", c="dimgray")

    def visualize(self, diagram_type: Any) -> None:
        if diagram_type not in ["hist", "violin", "box"]:
            raise ValueError

        axis_scatter, axis_horis, axis_vert = self._setup_figure_grid_axes()
        self._setup_scatter(axis_scatter)

        if diagram_type == "hist":
            histogram_plot(self._abscissa, axis_horis, is_horis=True)
            histogram_plot(self._ordinates, axis_vert, is_horis=False)
        elif diagram_type == "violin":
            violin_plot(self._abscissa, axis_horis, is_horis=True)
            violin_plot(self._ordinates, axis_vert, is_horis=False)
        else:
            box_plot(self._abscissa, axis_horis, is_horis=True)
            box_plot(self._ordinates, axis_vert, is_horis=False)


def histogram_plot(data: np.ndarray, axis: plt.Axes, is_horis: bool) -> None:
    axis.hist(
        data,
        bins=50,
        color="mediumseagreen",
        orientation="vertical" if is_horis else "horizontal",
        density=True,
        alpha=0.4,
    )

    if is_horis:
        axis.invert_yaxis()
    else:
        axis.invert_xaxis()


def violin_plot(data: np.ndarray, axis: plt.Axes, is_horis: bool) -> None:
    violin_parts = axis.violinplot(data, vert=False if is_horis else True, showmedians=True)

    for body in violin_parts["bodies"]:
        body.set_facecolor("mediumseagreen")
        body.set_edgecolor("green")

    for part in violin_parts:
        if part == "bodies":
            continue
        violin_parts[part].set_edgecolor("mediumseagreen")

    if is_horis:
        axis.set_yticks([])
    else:
        axis.set_xticks([])


def box_plot(data: np.ndarray, axis: plt.Axes, is_horis: bool) -> None:
    axis.boxplot(
        data,
        vert=False if is_horis else True,
        patch_artist=True,
        boxprops=dict(facecolor="mediumseagreen", alpha=0.6),
        medianprops=dict(color="k"),
    )

    if is_horis:
        axis.set_yticks([])
    else:
        axis.set_xticks([])


def visualize_diagrams(abscissa: np.ndarray, ordinates: np.ndarray, diagram_type: Any) -> None:
    visualizer = DiagramVisualizer(abscissa, ordinates, space)
    visualizer.visualize(diagram_type)


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
