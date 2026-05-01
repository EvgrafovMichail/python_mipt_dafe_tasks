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

    if len(abscissa) != len(ordinates):
        raise ShapeMismatchError(
            f"Длины массивов должны совпадать: abscissa={len(abscissa)}, ordinates={len(ordinates)}"
        )

    # проверка допустимости diagram_type
    valid_types = ["hist", "violin", "box"]
    if diagram_type not in valid_types:
        raise ValueError(
            f"diagram_type должен быть одним из: {valid_types}, получено '{diagram_type}'"
        )

    # Создаем фигуру с сеткой 2x2
    plt.figure(figsize=(10, 10))

    # Основная диаграмма рассеяния (нижний левый)
    scatter_ax = plt.subplot(2, 2, 3)
    scatter_ax.scatter(
        abscissa, ordinates, alpha=0.6, s=20, c="steelblue", edgecolors="white", linewidth=0.5
    )
    scatter_ax.set_xlabel("X")
    scatter_ax.set_ylabel("Y")
    scatter_ax.set_title("Диаграмма рассеяния")
    scatter_ax.grid(True, alpha=0.3)

    # Распределение по оси X (верхний левый)
    x_ax = plt.subplot(2, 2, 1)

    if diagram_type == "hist":
        x_ax.hist(abscissa, bins=30, color="steelblue", alpha=0.7, edgecolor="white")
        x_ax.set_title("Распределение по X (гистограмма)")

    elif diagram_type == "violin":
        x_ax.violinplot(abscissa, positions=[0], showmeans=True, showmedians=True)
        x_ax.set_title("Распределение по X (скрипичная диаграмма)")

    elif diagram_type == "box":
        x_ax.boxplot(abscissa, vert=True, positions=[0])
        x_ax.set_title("Распределение по X (ящик с усами)")

    x_ax.set_xlabel("X")
    x_ax.set_ylabel("Плотность")
    x_ax.grid(True, alpha=0.3)

    # Распределение по оси Y (нижний правый)
    y_ax = plt.subplot(2, 2, 4)

    if diagram_type == "hist":
        y_ax.hist(
            ordinates,
            bins=30,
            color="lightcoral",
            alpha=0.7,
            edgecolor="white",
            orientation="horizontal",
        )
        y_ax.set_title("Распределение по Y (гистограмма)")

    elif diagram_type == "violin":
        y_ax.violinplot(ordinates, positions=[0], vert=False, showmeans=True, showmedians=True)
        y_ax.set_title("Распределение по Y (скрипичная диаграмма)")

    elif diagram_type == "box":
        y_ax.boxplot(ordinates, vert=False, positions=[0])
        y_ax.set_title("Распределение по Y (ящик с усами)")

    y_ax.set_xlabel("Плотность")
    y_ax.set_ylabel("Y")
    y_ax.grid(True, alpha=0.3)

    # Убираем пустой угол (верхний правый)
    plt.subplot(2, 2, 2).axis("off")

    # Общий заголовок
    plt.suptitle(
        f"Визуализация данных\nТип распределения: {diagram_type}", fontsize=14, fontweight="bold"
    )

    # Автоматическая подгонка
    plt.tight_layout()


if __name__ == "__main__":
    mean = [2, 3]
    cov = [[1, 1], [1, 2]]
    space = 0.2

    abscissa, ordinates = np.random.multivariate_normal(mean, cov, size=1000).T

    visualize_diagrams(abscissa, ordinates, "hist")
    plt.show()
