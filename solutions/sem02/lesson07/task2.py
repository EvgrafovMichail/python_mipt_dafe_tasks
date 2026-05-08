# ваш код (используйте функции или классы для решения данной задачи)
import json

import matplotlib.pyplot as plt
import numpy as np


def get_counts(tier_list, stages_order):
    arr = np.array(tier_list)
    return np.array([np.sum(arr == stage) for stage in stages_order])


def solution():
    plt.style.use("ggplot")
    with open("solutions\sem02\lesson07\data\medic_data.json") as f:
        data = json.load(f)

    stages_order = ["I", "II", "III", "IV"]

    before_count = get_counts(data["before"], stages_order)
    after_count = get_counts(data["after"], stages_order)

    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(stages_order))
    width = 0.35

    ax.bar(x - width / 2, before_count, width, label="До установки", color="red", edgecolor="black")
    ax.bar(
        x + width / 2, after_count, width, label="После установки", color="green", edgecolor="black"
    )
    ax.set_title("Стадии митральной недостаточности")
    ax.set_ylabel("Кол-во людей")
    ax.set_xticks(x)
    ax.set_xticklabels(stages_order)
    ax.legend()
    fig.tight_layout()

    plt.savefig("result.png")
    plt.show()


if __name__ == "__main__":
    solution()
