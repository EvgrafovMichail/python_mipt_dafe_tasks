from json import load
from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def read_data(path: Any = "./data/medic_data.json") -> Any:
    with open(path) as file:
        data = load(file)

    return data


def get_amounts(data: np.array) -> np.array:
    data_amnt = np.array([data.count("I"), data.count("II"), data.count("III"), data.count("IV")])

    return data_amnt


def visualize_data(before: np.array, after: np.array) -> None:
    figure, axis = plt.subplots(figsize=(16, 8))

    stages = ["I", "II", "III", "IV"]
    x = np.arange(len(stages))
    width = 0.35

    axis.bar(x - width / 2, before, width, label="до установки импланта", color="red")

    axis.bar(x + width / 2, after, width, label="после установки импланта", color="green")

    axis.set_title("Степени митральной недостаточности", fontsize=16, fontweight="bold")

    axis.set_ylabel("Количество пациентов", fontweight="bold")
    axis.set_xticks(x)
    axis.set_xticklabels(stages, fontweight="bold")
    axis.tick_params(axis="both", labelcolor="dimgray")

    axis.legend(fontsize=12)

    plt.show()


def main():
    data = read_data("./data/medic_data.json")

    before_amounts = get_amounts(data["before"])
    after_amounts = get_amounts(data["after"])

    visualize_data(before_amounts, after_amounts)


if __name__ == "__main__":
    main()
