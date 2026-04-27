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
    
    valid_types = ("hist", "violin", "box")
    if diagram_type not in valid_types:
        raise ValueError
    
    picture = plt.figure(figsize=(12, 12))
    grid = plt.GridSpec(4, 4, wspace=space, hspace=space)

    main = picture.add_subplot(grid[:-1, 1:])
    left = picture.add_subplot(grid[:-1, 0], sharey=main)
    low = picture.add_subplot(grid[-1, 1:], sharex=main)

    main.scatter(abscissa, ordinates, color="m", alpha=0.7)

    if diagram_type == "hist":

        low.hist(
                abscissa,
                bins=75,
                color="m",
                density=True
        )

        left.hist(
                ordinates,
                bins=75,
                color="m",
                density=True,
                orientation="horizontal",
        )

        low.invert_yaxis()
        left.invert_xaxis()
    
    elif diagram_type == "violin":
        v_left = left.violinplot(
                ordinates, 
                vert=False, 
                showmedians=True
        )

        for body in v_left["bodies"]:
            body.set_facecolor("m")
            body.set_edgecolor("m")

        for part in v_left:
            if part != "bodies":
                v_left[part].set_edgecolor("m")

        v_low = low.violinplot(
                abscissa, 
                vert=True, 
                showmedians=True
        )

        for body in v_low["bodies"]:
            body.set_facecolor("m")
            body.set_edgecolor("m")

        for part in v_low:
            if part != "bodies":
                v_low[part].set_edgecolor("m")

        low.invert_yaxis()
        left.invert_xaxis()
        
    else:

        left.boxplot(ordinates, vert=False, patch_artist=True,
                     boxprops=dict(facecolor="m", alpha=0.7),
                     medianprops=dict(color="darkmagenta"),
                     whiskerprops=dict(color="m"),
                     capprops=dict(color="m"),
                     flierprops=dict(marker="o", markerfacecolor="m", markeredgecolor="m"))
        
        low.boxplot(abscissa, vert=True, patch_artist=True,
                       boxprops=dict(facecolor="m", alpha=0.7),
                       medianprops=dict(color="darkmagenta"),
                       whiskerprops=dict(color="m"),
                       capprops=dict(color="m"),
                       flierprops=dict(marker="o", markerfacecolor="m", markeredgecolor="m"))
        
        low.invert_yaxis()
        left.invert_xaxis()
        
    pass


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
