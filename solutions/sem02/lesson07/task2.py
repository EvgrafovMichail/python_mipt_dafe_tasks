import json

import matplotlib.pyplot as plt
import numpy as np

with open("data/medic_data.json", "r") as f:
    data_prew = json.load(f)

data1 = np.array(data_prew["before"])
labels, counts1 = np.unique(data1, return_counts=True)

data2 = np.array(data_prew["after"])
_, counts2 = np.unique(data2, return_counts=True)

abscissa = np.arange(len(labels))
width = 0.35

figure, axis = plt.subplots(figsize=(12, 7))

bl = axis.bar(
    abscissa - width / 1.9,
    counts1,
    width=width,
    label="Before",
    color="cornflowerblue",
    edgecolor="black",
    alpha=0.7,
)
br = axis.bar(
    abscissa + width / 1.9,
    counts2,
    width=width,
    label="After",
    color="mediumpurple",
    edgecolor="black",
    alpha=0.7,
)

axis.set_title("Mitral disease stages", fontsize=16, fontweight="bold", color="dimgray")
axis.set_ylabel("amount of people", fontsize=12, fontweight="bold", color="dimgray")
axis.set_xticks(abscissa)
axis.set_xticklabels(labels, fontsize=10, fontweight="bold", color="dimgray")
axis.legend()

axis.bar_label(bl, padding=3)
axis.bar_label(br, padding=3)

plt.savefig("my_analysis.png", dpi=300, bbox_inches="tight")
plt.show()
