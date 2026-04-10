import json
import matplotlib.pyplot as plt
import numpy as np


def read_from_file(filename: str) -> tuple[list[str], list[str]]:
    with open(filename, "r") as file:
        data = json.load(file)

    return data["before"], data["after"]


def get_counts_in_groups(before: list[str], after: list[str]) -> tuple[np.ndarray, np.ndarray]:
    count_before = np.unique(np.array(before), return_counts=True)[1]
    count_after = np.unique(after, return_counts=True)[1]

    return count_before, count_after


def set_labels_and_ticks(axis: plt.Axes) -> None:
    axis.set_title("Mitral disease stages", fontsize=17, fontweight="bold", c="dimgray")
    axis.set_xlabel("Group", fontsize=14, fontweight="bold", c="dimgray")
    axis.set_ylabel("Amount of people", fontsize=14, fontweight="bold", c="dimgray")

    labels = np.array(["I", "II", "III", "IV"])
    axis.set_xticks(np.arange(labels.size), labels=labels, fontweight="bold")
    axis.tick_params(axis="x", labelsize=14, labelcolor="dimgray")


def show_plots_and_legend(
    axis: plt.Axes, count_before: np.ndarray, count_after: np.ndarray
) -> None:
    shift = 0.2

    bar_before = axis.bar(
        np.arange(count_before.size) - shift,
        count_before,
        width=0.4,
        color="moccasin",
        edgecolor="orange",
    )
    bar_after = axis.bar(
        np.arange(count_after.size) + shift,
        count_after,
        width=0.4,
        color="orange",
        edgecolor="chocolate",
    )
    axis.legend((bar_before, bar_after), ["before", "after"])


def visualize(count_before: np.ndarray, count_after: np.ndarray) -> None:
    figure, axis = plt.subplots(figsize=(9, 9))
    axis: plt.Axes

    set_labels_and_ticks(axis)
    show_plots_and_legend(axis, count_before, count_after)
    plt.show()

    figure.savefig("Mitral disease stages.png", bbox_inches="tight")


if __name__ == "__main__":
    data = read_from_file("data/medic_data.json")
    counts = get_counts_in_groups(*data)
    visualize(*counts)
