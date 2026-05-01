import json

import matplotlib.pyplot as plt
import numpy as np


def count_by_stage(records: list) -> np.ndarray:
    stages = ["I", "II", "III", "IV"]
    counts = np.zeros(len(stages), dtype=int)
    for record in records:
        counts[stages.index(record)] += 1
    return counts


def build_bar_chart(
    before_counts: np.ndarray,
    after_counts: np.ndarray,
) -> None:
    figure, axis = plt.subplots(figsize=(16, 9))
    x = np.arange(4)

    axis.set_title(
        "Mitral disease stages",
        fontsize=17,
        fontweight="bold",
        c="dimgray",
    )
    axis.set_ylabel(
        "amount of people",
        fontsize=14,
        fontweight="bold",
        c="dimgray",
    )
    axis.set_xticks(x, labels=["I", "II", "III", "IV"], weight="bold")
    axis.tick_params(axis="x", labelsize=14, labelcolor="dimgray")

    axis.bar(
        x - 0.2, before_counts, width=0.35, color="mediumpurple", edgecolor="purple", label="before"
    )
    axis.bar(x + 0.2, after_counts, width=0.35, color="plum", edgecolor="purple", label="after")
    axis.legend(fontsize=14)

    figure.savefig("mitral_disease_stages.png")
    plt.show()


if __name__ == "__main__":
    plt.style.use("ggplot")
    with open("lesson07/data/medic_data.json") as f:
        data = json.load(f)
        before_counts = count_by_stage(data["before"])
        after_counts = count_by_stage(data["after"])
        build_bar_chart(before_counts, after_counts)
