import json

import matplotlib.pyplot as plt
import numpy as np


def download_data(path: str) -> tuple[np.ndarray, np.ndarray]:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    before = np.array(data["before"])
    after = np.array(data["after"])
    return (before, after)


def count_stages(arr: np.ndarray) -> list[int]:
    counts = []
    for stage in ["I", "II", "III", "IV"]:
        mask = arr == stage
        counts.append(sum(mask))
    return counts


def visualize_data(before: list[int], after: list[int]):
    plt.style.use("ggplot")
    stages = ["I", "II", "III", "IV"]
    poses = np.arange(len(stages))
    width = 0.4

    _, axes = plt.subplots(figsize=(9, 6))
    axes.bar(
        poses - width / 2, before, width, label="before", color="cornflowerblue", edgecolor="blue"
    )
    axes.bar(poses + width / 2, after, width, label="after", color="indianred", edgecolor="red")
    axes.set_xticks(poses)
    axes.set_xticklabels(stages)
    axes.set_ylabel("Amount of people")
    axes.set_title("Mitral disease stages")
    axes.legend()


if __name__ == "__main__":
    before, after = download_data(path="solutions/sem02/lesson07/data/medic_data.json")
    visualize_data(count_stages(before), count_stages(after))
    plt.show()
