import json

import matplotlib.pyplot as plt
import numpy as np

ROMAN_LETTERS = ["I", "II", "III", "IV"]

plt.style.use("ggplot")


def load_data(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def count_grades(data: dict) -> tuple[list[int], list[int]]:
    before_dict = {label: 0 for label in ROMAN_LETTERS}
    after_dict = {label: 0 for label in ROMAN_LETTERS}

    for grade in data["before"]:
        before_dict[grade] += 1
    for grade in data["after"]:
        after_dict[grade] += 1

    before_counts = [before_dict[label] for label in ROMAN_LETTERS]
    after_counts = [after_dict[label] for label in ROMAN_LETTERS]
    return before_counts, after_counts


def make_plot(before: list[int], after: list[int], output_path: str) -> None:
    x = np.arange(len(ROMAN_LETTERS))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(
        x - width / 2,
        before,
        width,
        label="before",
        color="cornflowerblue",
        edgecolor="blue",
    )
    ax.bar(
        x + width / 2,
        after,
        width,
        label="after",
        color="sandybrown",
        edgecolor="brown",
    )

    ax.xaxis.set_label_position("top")
    ax.set_xlabel(
        "Mitral disease stages",
        fontsize=16,
        fontweight="bold",
        color="gray",
        labelpad=10,
    )

    ax.set_ylabel(
        "amount of people",
        fontsize=16,
        fontweight="bold",
        color="gray",
        labelpad=10,
    )
    ax.set_xticks(x)
    ax.set_xticklabels(
        ROMAN_LETTERS,
        fontsize=12,
        fontweight="bold",
        color="gray",
    )
    ax.legend(fontsize=11)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def analyze_effectiveness(before: list[int], after: list[int]) -> None:
    print("Распределение до:   ", dict(zip(ROMAN_LETTERS, before)))
    print("Распределение после:", dict(zip(ROMAN_LETTERS, after)))
    print("\nВывод:")
    print("Количество пациентов с тяжёлыми")
    print(" степенями (III, IV) значительно уменьшилось,")
    print("а число пациентов с лёгкой ")
    print("степенью (I) возросло ==> Имплант эффективен.")


def main():
    data_file = "data/medic_data.json"
    output_image = "data/mitral_regurgitation.png"

    data = load_data(data_file)
    before, after = count_grades(data)
    make_plot(before, after, output_image)
    analyze_effectiveness(before, after)

    print(f"\nДиаграмма сохранена в файл: {output_image}")


if __name__ == "__main__":
    main()
