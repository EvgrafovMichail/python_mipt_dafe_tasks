from typing import Any

import matplotlib.gridspec as gs
import matplotlib.pyplot as plt
import numpy as np


class ShapeMismatchError(Exception):
    pass


def create_hist_sidebars(ordinates, abscissa, hsidebar, vsidebar, color):
    hsidebar.hist(
        ordinates, density=True, bins=50, histtype="stepfilled", orientation="vertical", color=color
    )
    vsidebar.hist(
        abscissa,
        density=True,
        bins=50,
        histtype="stepfilled",
        orientation="horizontal",
        color=color,
    )


def configure_violin_sidebar(violin_parts, color):
    for body in violin_parts["bodies"]:
        body.set_facecolor(color)
        body.set_edgecolor(color)

    for part in violin_parts:
        if part == "bodies":
            continue
        violin_parts[part].set_edgecolor(color)


def create_violin_sidebars(ordinates, abscissa, hsidebar, vsidebar, color):
    hviolin_parts = hsidebar.violinplot(abscissa, vert=False, showmedians=True)
    vviolin_parts = vsidebar.violinplot(ordinates, vert=True, showmedians=True)

    configure_violin_sidebar(hviolin_parts, color)
    configure_violin_sidebar(vviolin_parts, color)


def create_box_sidebars(ordinates, abscissa, hsidebar, vsidebar, color):
    hsidebar.boxplot(abscissa, vert=False, patch_artist=True, boxprops={"facecolor": color})
    vsidebar.boxplot(ordinates, vert=True, patch_artist=True, boxprops={"facecolor": color})


def visualize_diagrams(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    diagram_type: Any,
) -> None:
    if abscissa.shape != ordinates.shape:
        raise ShapeMismatchError

    dtypes = {
        "hist": create_hist_sidebars,
        "violin": create_violin_sidebars,
        "box": create_box_sidebars,
    }

    if diagram_type not in dtypes:
        raise ValueError

    figure = plt.figure(figsize=(7, 7))
    grid = gs.GridSpec(2, 2, width_ratios=[1, 3], height_ratios=[3, 1])

    vsidebar, axis, void, hsidebar = (figure.add_subplot(x) for x in grid)

    axis.scatter(abscissa, ordinates, c="blue")
    void.set_visible(False)

    hsidebar.invert_yaxis()
    vsidebar.invert_xaxis()

    dtypes[diagram_type](ordinates, abscissa, hsidebar, vsidebar, "blue")


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    plt.style.use("bmh")

    visualize_diagrams(abscissa, ordinates, "hist")

    plt.show()
