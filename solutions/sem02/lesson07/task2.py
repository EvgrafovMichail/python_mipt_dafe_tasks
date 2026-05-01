import json
import os
import typing

import matplotlib.pyplot as plt
import numpy as np


def read_data(file: str) -> typing.Tuple[np.ndarray, np.ndarray]:
    with open(file, "r") as f:
        data = json.load(f)
    return np.array(data["before"]), np.array(data["after"])


def process_data(before: np.ndarray, after: np.ndarray) -> typing.Tuple[np.ndarray, np.ndarray]:
    _, counts_before = np.unique(before, return_counts=True)
    _, counts_after = np.unique(after, return_counts=True)
    return counts_before, counts_after


def visualize(counts_before: np.ndarray, counts_after: np.ndarray) -> None:
    plt.style.use("fivethirtyeight")
    species = ("I", "II", "III", "IV")
    counts = {
        "Before": counts_before,
        "After": counts_after,
    }

    x = np.arange(len(species))
    width = 0.4
    multiplier = 0
    figure, axes = plt.subplots(figsize=(16, 9), layout="constrained")
    axes: plt.Axes

    for attribute, measurement in counts.items():
        offset = width * multiplier
        axes.bar(x + offset, measurement, width, label=attribute)
        multiplier += 1

    axes.set_ylabel("Amount of people")
    axes.set_title("Mitral disease stages")
    axes.set_xticks(x + width / 2, species)
    axes.legend(loc="upper right", ncols=3)

    plt.show()


if __name__ == "__main__":
    before, after = read_data(os.path.join(os.path.dirname(__file__), "data", "medic_data.json"))
    before_counts, after_counts = process_data(before, after)
    visualize(before_counts, after_counts)
