import json

import matplotlib.pyplot as plt
import numpy as np


def read_from_json(file_name: str) -> tuple[list[int], list[int]]:
    with open(file_name, "r") as file:
        data = json.load(file)

    before = data["before"]
    after = data["after"]

    return before, after


def get_counts_of_groups(before: list[int], after: list[int]) -> tuple[np.ndarray, np.ndarray]:
    labels_before, counts_before = np.unique(np.array(before), return_counts=True)
    labels_after, counts_after = np.unique(np.array(after), return_counts=True)

    return counts_before, counts_after


def visualize_diagrams(counts_before: np.ndarray, counts_after: np.ndarray):
    figure, axis = plt.subplots(figsize=(9, 9))
    axis: plt.Axes

    labels = np.array(["I", "II", "III", "IV"])

    bar1 = axis.bar(
        np.arange(counts_before.size) - 0.2,
        counts_before,
        color="peachpuff",
        edgecolor="orange",
        width=0.4,
    )
    bar2 = axis.bar(
        np.arange(counts_before.size) + 0.2,
        counts_after,
        color="plum",
        edgecolor="purple",
        width=0.4,
    )
    axis.set_xticks(
        np.arange(labels.size),
        labels=labels,
        weight="bold",
    )
    axis.tick_params(axis="x", labelsize=14, labelcolor="dimgray")

    axis.set_title("Mitral disease stages", fontsize=17, fontweight="bold", c="black")
    axis.set_xlabel("Groups", fontsize=14, fontweight="bold", c="dimgray")
    axis.set_ylabel("Amount of people", fontsize=14, fontweight="bold", c="dimgray")
    axis.legend((bar1, bar2), ["before", "after"])

    figure.savefig("Mitral disease stages.png", bbox_inches="tight")


if __name__ == "__main__":
    data = read_from_json("data/medic_data.json")
    counts = get_counts_of_groups(*data)
    visualize_diagrams(*counts)

    plt.show()
