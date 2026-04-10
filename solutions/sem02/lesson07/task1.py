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
        raise ShapeMismatchError("Razmery massivov ne sovpadayut")

    dopustimye_tipy = ("hist", "box", "violin")
    if diagram_type not in dopustimye_tipy:
        raise ValueError("Nedopustimyi tip diagrammy")

    figura = plt.figure(figsize=(8, 8))
    prosvet = 0.3
    setka = plt.GridSpec(4, 4, wspace=prosvet, hspace=prosvet)

    os_glavnaya = figura.add_subplot(setka[:-1, 1:])
    os_glavnaya.scatter(abscissa, ordinates, color="seagreen", alpha=0.5, s=15)

    if diagram_type == "hist":
        os_v = figura.add_subplot(setka[:-1, 0], sharey=os_glavnaya)
        os_g = figura.add_subplot(setka[-1, 1:], sharex=os_glavnaya)

        os_g.hist(abscissa, bins=50, color="indianred", alpha=0.6, density=True)
        os_v.hist(
            ordinates, bins=50, color="indianred", alpha=0.6, density=True, orientation="horizontal"
        )

        os_g.invert_yaxis()
        os_v.invert_xaxis()

    elif diagram_type == "violin":
        os_v = figura.add_subplot(setka[:-1, 0], sharey=os_glavnaya)
        os_g = figura.add_subplot(setka[-1, 1:], sharex=os_glavnaya)

        os_v.violinplot(ordinates, vert=True, showmedians=True)
        os_g.violinplot(abscissa, vert=False, showmedians=True)

        os_g.invert_yaxis()
        os_v.invert_xaxis()

    elif diagram_type == "box":
        os_v = figura.add_subplot(setka[:-1, 0], sharey=os_glavnaya)
        os_g = figura.add_subplot(setka[-1, 1:], sharex=os_glavnaya)

        os_v.boxplot(ordinates, vert=True, patch_artist=True)
        os_g.boxplot(abscissa, vert=False, patch_artist=True)

        os_g.invert_yaxis()
        os_v.invert_xaxis()

    plt.show()


if __name__ == "__main__":
    x = np.random.normal(2, 1, 1000)
    y = x + np.random.normal(1, 1, 1000)

    visualize_diagrams(x, y, "hist")
