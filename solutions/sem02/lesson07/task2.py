import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def visualize_mitral_regurgitation(json_path: str = "medic_data.json") -> None:
    json_path = Path(__file__).parent / "data" / "medic_data.json"
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    before_data = data["before"]
    after_data = data["after"]

    levels = ["I", "II", "III", "IV"]

    before_counts = Counter(before_data)
    after_counts = Counter(after_data)

    before_values = [before_counts.get(level, 0) for level in levels]
    after_values = [after_counts.get(level, 0) for level in levels]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    purple_colors = ["#E6E6FA", "#9370DB", "#8A2BE2", "#4B0082"]
    teal_colors = ["#E0FFFF", "#7FFFD4", "#40E0D0", "#008080"]

    x_pos = np.arange(len(levels))
    bar_width = 0.7

    bars_before = ax1.bar(
        x_pos,
        before_values,
        width=bar_width,
        color=purple_colors,
        edgecolor="#4B0082",
        linewidth=2,
        alpha=0.85,
    )

    total_before = sum(before_values)
    for bar, value in zip(bars_before, before_values):
        height = bar.get_height()
        percentage = (value / total_before * 100) if total_before > 0 else 0
        ax1.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + max(before_values) * 0.02,
            f"{value}\n({percentage:.1f}%)",
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold",
            color="#4B0082",
        )

    ax1.set_xlabel(
        "Степень митральной недостаточности", fontsize=14, fontweight="bold", color="#4B0082"
    )
    ax1.set_ylabel("Количество пациентов", fontsize=14, fontweight="bold", color="#4B0082")
    ax1.set_title("ДО установки импланта", fontsize=16, fontweight="bold", color="#4B0082", pad=15)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(levels, fontsize=13, fontweight="bold")
    ax1.grid(True, axis="y", alpha=0.3, linestyle="--", color="#9370DB")
    ax1.set_ylim(0, max(before_values) * 1.2)

    severity_descriptions = ["Легкая", "Умеренная", "Тяжелая", "Критическая"]
    for i, desc in enumerate(severity_descriptions):
        ax1.text(
            i,
            -max(before_values) * 0.08,
            desc,
            ha="center",
            fontsize=10,
            style="italic",
            color="#666666",
        )

    bars_after = ax2.bar(
        x_pos,
        after_values,
        width=bar_width,
        color=teal_colors,
        edgecolor="#008080",
        linewidth=2,
        alpha=0.85,
    )

    total_after = sum(after_values)
    for bar, value in zip(bars_after, after_values):
        height = bar.get_height()
        percentage = (value / total_after * 100) if total_after > 0 else 0
        ax2.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + max(after_values) * 0.02,
            f"{value}\n({percentage:.1f}%)",
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold",
            color="#008080",
        )

    ax2.set_xlabel(
        "Степень митральной недостаточности", fontsize=14, fontweight="bold", color="#008080"
    )
    ax2.set_ylabel("Количество пациентов", fontsize=14, fontweight="bold", color="#008080")
    ax2.set_title(
        "ПОСЛЕ установки импланта", fontsize=16, fontweight="bold", color="#008080", pad=15
    )
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(levels, fontsize=13, fontweight="bold")
    ax2.grid(True, axis="y", alpha=0.3, linestyle="--", color="#40E0D0")
    ax2.set_ylim(0, max(after_values) * 1.2)

    for i, desc in enumerate(severity_descriptions):
        ax2.text(
            i,
            -max(after_values) * 0.08,
            desc,
            ha="center",
            fontsize=10,
            style="italic",
            color="#666666",
        )

    fig.suptitle(
        "Анализ эффективности кардио-импланта\nпри митральной недостаточности",
        fontsize=18,
        fontweight="bold",
        color="#333333",
        y=1.02,
    )

    plt.tight_layout()
    plt.show()


visualize_mitral_regurgitation()
