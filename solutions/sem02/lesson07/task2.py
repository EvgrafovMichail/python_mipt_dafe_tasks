import json

import matplotlib.pyplot as plt
import numpy as np


def solve_cardio_task(file_path: str) -> tuple[np.ndarray, np.ndarray]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    stages = ["I", "II", "III", "IV"]

    def get_stage_counts(values: list[str]) -> list[int]:
        stage_array = np.array(values)
        unique_stages, counts = np.unique(stage_array, return_counts=True)
        counts_by_stage = dict(zip(unique_stages, counts))
        return [counts_by_stage.get(stage, 0) for stage in stages]

    before = get_stage_counts(data["before"])
    after = get_stage_counts(data["after"])

    positions = np.arange(len(stages))
    width = 0.35

    plt.style.use("ggplot")
    figure, axis = plt.subplots(figsize=(10, 6))

    before_bars = axis.bar(
        positions - width / 2,
        before,
        width,
        label="Before",
        color="lightsteelblue",
        edgecolor="royalblue",
    )
    after_bars = axis.bar(
        positions + width / 2,
        after,
        width,
        label="After",
        color="salmon",
        edgecolor="crimson",
    )

    axis.set_ylabel("Patients count", fontsize=12)
    axis.set_title(
        "Mitral insufficiency stages",
        fontsize=14,
        fontweight="bold",
    )
    axis.set_xticks(positions, labels=stages)
    axis.legend()
    axis.grid()
    axis.bar_label(before_bars)
    axis.bar_label(after_bars)

    plt.savefig("heart_implant_efficiency.png", dpi=300)
    plt.show()

    return np.array(before), np.array(after)


if __name__ == "__main__":
    before_counts, after_counts = solve_cardio_task("data/medic_data.json")

    if after_counts[0] + after_counts[1] > before_counts[0] + before_counts[1]:
        print(
            "Имплант можно считать эффективным: после установки стало больше пациентов "
            "с лёгкими стадиями I-II и меньше пациентов с тяжёлыми стадиями III-IV."
        )
