import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def get_counts(tier_list, stages_list):
    arr = np.array(tier_list)
    return np.array([np.sum(arr == stage) for stage in stages_list])


def heart_task():
    plt.style.use("ggplot")
    
    with open("solutions\sem02\lesson07\data\medic_data.json") as file:
        data = json.load(file)

    stages_list = ["I", "II", "III", "IV"]
    before_count = get_counts(data["before"], stages_list)
    after_count = get_counts(data["after"], stages_list)
    
    fig, ax = plt.subplots(figsize=(10, 7))
    x = np.arange(len(stages_list))
    width = 0.25

    ax.bar(x - width / 2, before_count, width, label="before", color="lightcoral", edgecolor="darkred")
    ax.bar(x + width / 2, after_count, width, label="after", color="cornflowerblue", edgecolor="darkblue")
    
    ax.set_title("Стадии митральной недостаточности")
    ax.set_ylabel("Количество больных")
    ax.set_xticks(x)
    ax.set_xticklabels(stages_list)
    ax.legend()
    fig.tight_layout()

    plt.savefig("solutions/sem02/lesson07/data/result.png")
    plt.show()


if __name__ == "__main__":
    heart_task()