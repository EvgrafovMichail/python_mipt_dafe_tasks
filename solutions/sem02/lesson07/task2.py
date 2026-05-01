import json

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

with open("solutions\sem02\lesson07\data\medic_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def medic_diagram(data):
    labels, counts_before = np.unique(np.array(data["before"]), return_counts=True)
    labels, counts_after = np.unique(np.array(data["after"]), return_counts=True)

    figure, axis = plt.subplots(figsize=(8, 8))
    width = 0.3

    axis.bar(
        np.arange(labels.size) - width / 2,
        counts_before,
        width=width,
        color="lightpink",
        edgecolor="palevioletred",
        label="before",
    )

    axis.bar(
        np.arange(labels.size) + width / 2,
        counts_after,
        width=width,
        color="hotpink",
        edgecolor="palevioletred",
        label="after",
    )

    axis.set_title("Mitral disease stages", fontsize=17, fontweight="bold", c="orchid")
    axis.set_xticks(np.arange(labels.size), labels=labels, weight="bold")
    axis.set_ylabel("amount of people", fontsize=14, fontweight="bold", c="orchid")
    axis.legend(fontsize=15)

    figure.savefig("solutions/sem02/lesson07/medic_diagram.png", bbox_inches="tight")


medic_diagram(data)

"""
Количество людей с III и IV степепнью заболевания значительно уменьшилось.
Степень заболевания многих из них вероятно понизилась.
Имплант можно считать эффективным.
 
"""
