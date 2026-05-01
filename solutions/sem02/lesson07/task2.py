# ваш код (используйте функции или классы для решения данной задачи)
import json
import os

import matplotlib.pyplot as plt
import numpy as np


def get_data_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "data", "medic_data.json")


def get_output_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "task2_result.png")


def load_data(filepath: str) -> dict:
    with open(filepath, "r") as file:
        return json.load(file)


def count_stages(data: list) -> dict:
    counts = {"I": 0, "II": 0, "III": 0, "IV": 0}
    for item in data:
        if item in counts:
            counts[item] += 1
    return counts


def prepare_data(data_dict: dict) -> tuple:
    before_counts = count_stages(data_dict["before"])
    after_counts = count_stages(data_dict["after"])

    stages = ["I", "II", "III", "IV"]
    before_values = [before_counts[s] for s in stages]
    after_values = [after_counts[s] for s in stages]

    return stages, before_values, after_values


def create_visualization(stages: list, before: list, after: list, output_path: str) -> None:
    figure, axis = plt.subplots(figsize=(16, 9))

    x = np.arange(len(stages))
    width = 0.35

    axis.bar(
        x - width / 2,
        before,
        width,
        label="before",
        color="mediumseagreen",
        edgecolor="seagreen",
    )

    axis.bar(
        x + width / 2,
        after,
        width,
        label="after",
        color="mediumpurple",
        edgecolor="rebeccapurple",
    )

    axis.set_ylabel("amount of people", fontsize=18, fontweight="bold", c="dimgray")
    axis.set_title(
        "Mitral disease stages",
        fontsize=24,
        fontweight="bold",
        c="dimgray",
    )
    axis.set_xticks(x, labels=stages, weight="bold")
    axis.tick_params(axis="x", labelsize=18, labelcolor="dimgray")
    axis.tick_params(axis="y", labelsize=14, labelcolor="dimgray")
    axis.legend(fontsize=20)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.show()


def analyze_results(before: list, after: list) -> str:
    severe_before = before[2] + before[3]
    severe_after = after[2] + after[3]

    if severe_after < severe_before:
        return "Имплант эффективен: доля тяжелых стадий (III-IV) снизилась."
    elif severe_after > severe_before:
        return "Имплант неэффективен: доля тяжелых стадий (III-IV) выросла."
    else:
        return "Эффект импланта не выражен: доля тяжелых стадий не изменилась."


def main():
    data_path = get_data_path()
    output_path = get_output_path()

    data = load_data(data_path)
    stages, before, after = prepare_data(data)
    create_visualization(stages, before, after, output_path)

    conclusion = analyze_results(before, after)
    print(conclusion)


if __name__ == "__main__":
    main()
