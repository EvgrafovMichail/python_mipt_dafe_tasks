import json

import matplotlib.pyplot as plt
import numpy as np


def visualise_progress(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "before" not in data or "after" not in data:
        raise ValueError("wrong data format")

    all_labels = ["I", "II", "III", "IV"]
    counts_before = [data["before"].count(symb) for symb in all_labels]
    counts_after = [data["after"].count(symb) for symb in all_labels]
    stages = np.arange(4)
    width = 0.4

    plt.style.use("seaborn-v0_8-darkgrid")
    figure, axis = plt.subplots(figsize=(12, 7))

    axis.set_title("Mitral diseases stages", fontsize=17, fontweight="bold", c="dimgray")
    axis.set_ylabel("amount of people", fontsize=15, fontweight="bold", c="dimgray")
    axis.set_xlabel("stages of diseases", fontsize=15, fontweight="bold", c="dimgray")

    axis.tick_params(axis="x", labelsize=14, labelcolor="dimgray")

    axis.bar(
        stages - width / 2,
        counts_before,
        width=width,
        color="green",
        edgecolor="limegreen",
        label="before",
    )
    axis.bar(
        stages + width / 2,
        counts_after,
        width=width,
        color="tomato",
        edgecolor="red",
        label="after",
    )
    axis.set_xticks(
        stages,
        labels=all_labels,
        weight="bold",
    )
    axis.legend(fontsize=15)

    figure.savefig("cardio_progress.png", bbox_inches="tight")
    plt.show()
