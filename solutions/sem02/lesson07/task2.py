import json
import os

import matplotlib.pyplot as plt
import numpy as np


def get_dict(file_name: str):
    script_dir = os.path.dirname(__file__)
    joined_path = os.path.join(script_dir, "data", file_name)
    with open(joined_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_arrays(data: dict, mask: dict):
    before = np.array([mask[x] for x in data["before"]])
    after = np.array([mask[x] for x in data["after"]])

    _, before_counts = np.unique(before, return_counts=True)
    _, after_counts = np.unique(after, return_counts=True)
    return before_counts, after_counts


def draw_diagram():
    mask = {"I": 1, "II": 2, "III": 3, "IV": 4}
    data = get_dict("medic_data.json")
    before_counts, after_counts = get_arrays(data, mask)

    _, axes = plt.subplots(ncols=2, sharey=True)
    axes[0].set_facecolor("#f2b1e8")
    axes[1].set_facecolor("#f2b1e8")

    axes[0].barh(list(mask.keys()), before_counts, color="#B40097", align="center")
    axes[0].set_title("Before")
    axes[0].invert_xaxis()

    axes[1].barh(list(mask.keys()), after_counts, color="#7C0C53", align="center")
    axes[1].set_title("After")
    axes[1].tick_params(axis="y", length=0)

    plt.subplots_adjust(wspace=0)
    plt.savefig("Diagram.png")
    plt.show()


if __name__ == "__main__":
    draw_diagram()


# самый главный вывод, по моему мнению, тот факт, что
# количество пациентов с тежелыми (3-4) степенями
# заболевания снизилась значительно
