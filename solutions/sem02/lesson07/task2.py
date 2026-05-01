import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def load_data() -> tuple:

    cur_dir = Path(__file__).parent
    file_path = cur_dir / "data" / "medic_data.json"

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    convert = {"I": 1, "II": 2, "III": 3, "IV": 4}
    before = [convert[grade] for grade in data["before"]]
    after = [convert[grade] for grade in data["after"]]

    return before, after


def count_by_grade(data: list) -> list:
    numbers = [0, 0, 0, 0]
    for grade in data:
        if 1 <= grade <= 4:
            numbers[grade - 1] += 1
    return numbers


def draw_chart(before_counts: list, after_counts: list) -> None:

    classes = [
        "I Stadium (stage)",
        "II Stadium (stage)",
        "III Stadium (stage)",
        "IV Stadium (stage)",
    ]
    x = np.arange(len(classes))
    width = 0.35

    _, ax = plt.subplots(figsize=(12, 6))

    histo1 = ax.bar(
        x - width / 2,
        before_counts,
        width,
        label="Vor der Installation (before installation)",
        color="steelblue",
        edgecolor="navy",
    )

    histo2 = ax.bar(
        x + width / 2,
        after_counts,
        width,
        label="Nach der Installation (after installation)",
        color="lightcoral",
        edgecolor="darkred",
    )

    ax.set_xlabel(
        "Stadien der Mitralkrankheit (Mitral disease stages)", fontsize=12, fontweight="bold"
    )

    ax.set_ylabel("Anzahl der Patienten (Number of patients)", fontsize=12, fontweight="bold")

    ax.set_title("Patientenstatistiken\n(Patient statistics)", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(classes)
    ax.legend(loc="upper right", fontsize=11)

    ax.grid(True, axis="y", linestyle="--", alpha=0.5)

    for bar in histo1:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1,
            str(int(height)),
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    for bar in histo2:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1,
            str(int(height)),
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    plt.tight_layout()

    plt.show()


def main():
    before, after = load_data()
    before_counts = count_by_grade(before)
    after_counts = count_by_grade(after)

    draw_chart(before_counts, after_counts)


if __name__ == "__main__":
    main()
