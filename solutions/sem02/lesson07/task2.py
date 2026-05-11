import json

import matplotlib.pyplot as plt
import numpy as np


def mitrial_disiase_analyse(path_to_json):
    with open(path_to_json, "r", encoding="utf-8") as f:
        data_dict = json.load(f)

    before_data = np.array(data_dict["before"])
    after_data = np.array(data_dict["after"])

    _, counts_before = np.unique(before_data, return_counts=True)
    _, counts_after = np.unique(after_data, return_counts=True)

    fig, axis = plt.subplots(figsize=(9, 9))
    axis: plt.Axes
    labels = np.array(["I", "II", "III", "IV"])

    x = np.arange(labels.size)
    width = 0.35

    axis.set_title("анализ заболевания", fontsize=17,)
    axis.set_ylabel("кол-во людей", fontsize=12)

    axis.bar(
        x - width / 2,
        counts_before,
        width=width,
        color="red",
        edgecolor="red",
        label="before",
    )
    axis.bar(
        x + width / 2,
        counts_after,
        width=width,
        color="blue",
        edgecolor="blue",
        label="after",
    )

    axis.set_xticks(x, labels=labels, weight="bold")
    axis.tick_params(axis="x", labelsize=14, labelcolor="dimgray")
    axis.legend()

    plt.savefig("mitral_disease_analysis.png")

