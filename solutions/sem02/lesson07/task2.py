import json

import matplotlib.pyplot as plt
import numpy as np


def mitral_disease_histogram() -> None:
    with open("data/medic_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    before = data["before"]
    after = data["after"]

    stages = ["I", "II", "III", "IV"]
    before_counts = [before.count(stage) for stage in stages]
    after_counts = [after.count(stage) for stage in stages]

    axis = plt.subplots(figsize=(10, 6))[-1]

    axis.grid(axis="y", alpha=0.3, color="black")

    x = np.arange(len(stages))
    width = 0.4

    axis.bar(
        x - width / 2,
        before_counts,
        width=width,
        label="before",
        color="skyblue",
        alpha=0.7,
        edgecolor="blue",
    )
    axis.bar(
        x + width / 2,
        after_counts,
        width=width,
        label="after",
        color="lightcoral",
        alpha=0.7,
        edgecolor="red",
    )

    axis.set_ylabel("amount of peple", fontweight="bold")
    axis.set_title("Mitral disease stages", fontweight="bold")
    axis.set_xticks(x)
    axis.set_xticklabels([stage for stage in stages])
    for label in axis.get_xticklabels():
        label.set_fontweight("bold")
    axis.legend()

    plt.savefig("mitral_insufficiency_analysis.png", dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    mitral_disease_histogram()

    plt.show()
