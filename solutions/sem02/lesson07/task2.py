import json

import matplotlib.pyplot as plt
import numpy as np


def get_data_for_plot(file_path: str) -> tuple[np.ndarray, np.ndarray]:
    with open(file_path, "r") as f:
        data = json.load(f)
    before = np.array(data["before"])
    after = np.array(data["after"])
    return before, after


def sum_classes(before: np.ndarray, after: np.ndarray, classes=["I", "II", "III", "IV"]):
    before_sum = {}
    after_sum = {}
    for cl in classes:
        mask = before == cl
        before_sum[cl] = np.sum(mask)
        mask = after == cl
        after_sum[cl] = np.sum(mask)
    return before_sum, after_sum


classes = ["I", "II", "III", "IV"]
before, after = get_data_for_plot("data/medic_data.json")
before_sum, after_sum = sum_classes(before, after)

fig, ax = plt.subplots(figsize=(9, 6))
x = np.arange(len(classes))
ax.tick_params(labelsize=16)

width = 0.35
bars1 = ax.bar(x - width / 2, before_sum.values(), width, label="before", color="cornflowerblue")
bars2 = ax.bar(x + width / 2, after_sum.values(), width, label="after", color="sandybrown")

ax.set_xlabel("Mitral disease stage", fontsize=16)
ax.set_ylabel("Amount of people", fontsize=16)
ax.set_title("Mitral disease stages", fontsize=16)
ax.grid(axis="y", color="#cacaca", linewidth=0.8)
ax.set_axisbelow(True)
ax.set_xticks(x)
ax.set_xticklabels(classes)
ax.legend(fontsize=16)

plt.savefig("class_distribution.png")
plt.show()
