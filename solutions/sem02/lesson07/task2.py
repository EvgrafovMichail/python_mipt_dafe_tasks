import json

import matplotlib.pyplot as plt
import numpy as np


def solve_cardio_task(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    stages = ["I", "II", "III", "IV"]

    def get_ordered_counts(data_list):
        arr = np.array(data_list)
        unique_vals, counts = np.unique(arr, return_counts=True)
        count_dict = dict(zip(unique_vals, counts))
        return [count_dict.get(s, 0) for s in stages]

    before_values = get_ordered_counts(data["before"])
    after_values = get_ordered_counts(data["after"])

    x = np.arange(len(stages))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))

    rects1 = ax.bar(
        x - width / 2,
        before_values,
        width,
        label="До установки",
        color="lightsteelblue",
        edgecolor="royalblue",
    )
    rects2 = ax.bar(
        x + width / 2,
        after_values,
        width,
        label="После установки",
        color="salmon",
        edgecolor="crimson",
    )

    ax.set_ylabel("Количество пациентов", fontsize=12)
    ax.set_title(
        "Распределение степеней митральной недостаточности", fontsize=14, fontweight="bold"
    )
    ax.set_xticks(x, labels=stages)
    ax.legend()

    ax.grid()

    ax.bar_label(rects1)
    ax.bar_label(rects2)

    plt.savefig("heart_implant_efficiency.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    solve_cardio_task("data/medic_data.json")

    """
    Общее количество пациентов перераспределилось из правой части графика (тяжелые состояния)
    в левую (легкие состояния), поэтому имплант можно считать эффективным
    и рекомендовать к серийному производству.
    """
