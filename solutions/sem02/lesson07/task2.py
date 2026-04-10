import json

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")


def apply_custom_style(ax):
    ax.set_facecolor("#F0F0F0")
    ax.grid(True, color="#A5A5A51B", linestyle="-", linewidth=0.5)
    ax.set_axisbelow(True)


def draw_mitral_diagram(ax: plt.Axes, categories: list[str], before: list[int], after: list[int]):
    x = np.arange(len(categories))
    width = 0.4
    colors = ["#F772C6", "#1CEED2", "#080808"]
    labels = ["До установки импланта", "После установки импланта"]
    apply_custom_style(ax)

    column1 = ax.bar(x - width / 2, before, width, label=labels[0], color=colors[0])
    column2 = ax.bar(x + width / 2, after, width, label=labels[1], color=colors[1])

    ax.set_title("Эффективность импланта при митральной недостаточности")
    ax.set_ylabel("Количество пациентов", color=colors[2])
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()

    ax.bar_label(column1)
    ax.bar_label(column2)


def visualize_medic_data(f_path: str):
    with open(f_path, "r") as f:
        data = json.load(f)

    deg_mitral_reg = ["I", "II", "III", "IV"]
    before_impl_ins = [data["before"].count(i) for i in deg_mitral_reg]
    after_impl_ins = [data["after"].count(i) for i in deg_mitral_reg]

    fig, ax = plt.subplots(figsize=(10, 6))
    draw_mitral_diagram(ax, deg_mitral_reg, before_impl_ins, after_impl_ins)

    fig.savefig("solutions/sem02/lesson07/medic_hist.png", bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    visualize_medic_data("solutions/sem02/lesson07/data/medic_data.json")
