import json

import matplotlib.pyplot as plt
import numpy as np


def get_counts_of_groups(before: list, after: list) -> tuple[np.ndarray, np.ndarray]:
    mapping = {"I": 0, "II": 1, "III": 2, "IV": 3}

    def to_indices(data):
        indices = []
        for item in data:
            val = mapping.get(str(item).upper(), int(item) - 1 if str(item).isdigit() else 0)
            indices.append(val)
        return np.array(indices)

    counts_before = np.bincount(to_indices(before), minlength=4)
    counts_after = np.bincount(to_indices(after), minlength=4)

    return counts_before, counts_after


def add_labels(axis: plt.Axes):
    text_param = {"fontsize": 17, "fontweight": "bold"}
    axis.set_title("Mitral disease stages", c="black", **text_param)
    axis.set_xlabel("Groups", c="dimgray", **text_param)
    axis.set_ylabel("Amount of people", c="dimgray", **text_param)


def visualize_diagrams(counts_before: np.ndarray, counts_after: np.ndarray):
    figure, axis = plt.subplots(figsize=(9, 9))

    labels = ["I", "II", "III", "IV"]
    x = np.arange(len(labels))
    width = 0.4

    bar1 = axis.bar(
        x - width / 2, counts_before, width, label="before", color="skyblue", edgecolor="purple"
    )
    bar2 = axis.bar(
        x + width / 2, counts_after, width, label="after", color="salmon", edgecolor="purple"
    )

    axis.set_xticks(x)
    axis.set_xticklabels(labels, weight="bold")
    axis.tick_params(axis="x", labelsize=14, labelcolor="dimgray")

    add_labels(axis)
    axis.legend(prop={"size": 14})
    axis.yaxis.grid(True, linestyle="--", alpha=0.6)
    axis.set_axisbelow(True)

    figure.savefig("Mitral disease stages.png", bbox_inches="tight")
    plt.show()


def main():
    with open("medic_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    before_counts, after_counts = get_counts_of_groups(data["before"], data["after"])

    visualize_diagrams(before_counts, after_counts)


if __name__ == "__main__":
    main()
