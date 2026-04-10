import json

import matplotlib.pyplot as plt
import numpy as np


def mitrial_disiase_analyse(path_to_json):
    with open(path_to_json, "r", encoding="utf-8") as f:
        data_dict = json.load(f)

    before = np.array(data_dict["before"])
    after = np.array(data_dict["after"])

    _, before_counts = np.unique(before, return_counts=True)
    _, after_counts = np.unique(after, return_counts=True)

    figure, axis = plt.subplots(figsize=(9, 9))
    axis: plt.Axes

    labels = np.array(["I", "II", "III", "IV"])

    x = np.arange(labels.size)
    width = 0.35

    axis.set_title("mitrial disiase analyse", fontsize=17, fontweight="bold", c="dimgray")
    axis.set_ylabel("amount of people", fontsize=14, fontweight="bold", c="dimgray")

    axis.bar(
        x - width / 2,
        before_counts,
        width=width,
        color="red",
        edgecolor="red",
        label="before",
    )
    axis.bar(
        x + width / 2,
        after_counts,
        width=width,
        color="blue",
        edgecolor="blue",
        label="after",
    )

    axis.set_xticks(x, labels=labels, weight="bold")
    axis.tick_params(axis="x", labelsize=14, labelcolor="dimgray")
    axis.legend()

    plt.savefig("mitral_disease_analysis.png", dpi=300, bbox_inches="tight")


# количество людей с терпимыми стадиями (1-2) увеличилось,
# а количество людей с опасными стадиями (3-4) уменьшилось,
# значит все в порядке и импланты работают как надо
