import json

import matplotlib.pyplot as plt
import numpy as np


def load(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    before = data["before"]
    after = data["after"]

    return before, after


def visualize(before, after):
    roman = ["I", "II", "III", "IV"]

    counts_before = []
    counts_after = []

    for r in roman:
        counts_before.append(before.count(r))
        counts_after.append(after.count(r))

    x = np.arange(len(roman))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(
        x - width / 2,
        counts_before,
        width,
        label="Before",
        color="mistyrose",
        edgecolor="darkred",
    )
    ax.bar(
        x + width / 2,
        counts_after,
        width,
        label="After",
        color="thistle",
        edgecolor="darkblue",
    )

    ax.set_ylabel("Amount of people")
    ax.set_title("Mitral disease stages")
    ax.set_xticks(x)
    ax.set_xticklabels(roman)
    ax.legend()

    fig.savefig("mitral_.png", bbox_inches="tight")

    plt.show()


def main():
    before, after = load("data/medic_data.json")
    visualize(before, after)


if __name__ == "__main__":
    main()


"""Имплантат больше всего эффективен для людей со 2,3,4 степенями митральной недостаточности. 
Количество людей с лёгкой степенью после только увеличилось. """
