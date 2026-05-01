import json

import matplotlib.pyplot as plt
import numpy as np


def visualize_diagrams(filepath: str) -> None:
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    roman_to_number = {"I": 1, "II": 2, "III": 3, "IV": 4}

    before_numbers = [roman_to_number[x] for x in data["before"]]
    after_numbers = [roman_to_number[x] for x in data["after"]]

    before_counts = [before_numbers.count(i) for i in range(1, 5)]
    after_counts = [after_numbers.count(i) for i in range(1, 5)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    x = np.arange(4)
    categories = ["I", "II", "III", "IV"]

    ax1.bar(x, before_counts, color="steelblue", edgecolor="white", linewidth=2)
    ax1.set_title("До установки импланта", fontsize=14, fontweight="bold")
    ax1.set_xlabel("Степень митральной недостаточности", fontsize=11)
    ax1.set_ylabel("Количество пациентов", fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, fontsize=10)
    ax1.grid(axis="y", alpha=0.3, linestyle="--")

    for bar, count in zip(ax1.bar(x, before_counts, color="steelblue"), before_counts):
        ax1.text(
            bar.get_x() + bar.get_width() / 2.0,
            count + 0.5,
            str(count),
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    ax2.bar(x, after_counts, color="lightcoral", edgecolor="white", linewidth=2)
    ax2.set_title("После установки импланта", fontsize=14, fontweight="bold")
    ax2.set_xlabel("Степень митральной недостаточности", fontsize=11)
    ax2.set_ylabel("Количество пациентов", fontsize=11)
    ax2.set_xticks(x)
    ax2.set_xticklabels(categories, fontsize=10)
    ax2.grid(axis="y", alpha=0.3, linestyle="--")

    for bar, count in zip(ax2.bar(x, after_counts, color="lightcoral"), after_counts):
        ax2.text(
            bar.get_x() + bar.get_width() / 2.0,
            count + 0.5,
            str(count),
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    plt.suptitle(
        "Распределение пациентов по степени митральной недостаточности\n" \
        "до и после установки кардио-импланта",
        fontsize=16,
        fontweight="bold",
    )

    plt.tight_layout()
    plt.savefig("mitral_insufficiency_distribution.png", dpi=150, bbox_inches="tight")
    plt.show()

    total_before = sum(before_counts)
    total_after = sum(after_counts)

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЭФФЕКТИВНОСТИ ИМПЛАНТА")
    print("=" * 60)

    for i, grade in enumerate(categories):
        before_pct = (before_counts[i] / total_before) * 100
        after_pct = (after_counts[i] / total_after) * 100
        change = after_pct - before_pct
        arrow = "↑" if change > 0 else "↓" if change < 0 else "→"
        print(
            f"{grade} степень: {before_pct:5.1f}% → {after_pct:5.1f}% ({arrow} {abs(change):.1f}%)"
        )

    severe_before = before_counts[2] + before_counts[3]
    severe_after = after_counts[2] + after_counts[3]

    print("\n" + "=" * 60)
    print("ВЫВОД:")
    print("=" * 60)

    if severe_before > 0:
        reduction = ((severe_before - severe_after) / severe_before) * 100
        if reduction > 30:
            print(f"✅ Имплант эффективен! Снижение тяжелых форм на {reduction:.1f}%")
        elif reduction > 10:
            print(f"⚠️ Имплант умеренно эффективен (снижение на {reduction:.1f}%)")
        else:
            print(f"❌ Имплант малоэффективен (снижение на {reduction:.1f}%)")


if __name__ == "__main__":
    visualize_diagrams("medic_data.json")
