import json

import matplotlib.pyplot as plt
import numpy as np

with open("data/medic_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
before = data["before"]
after = data["after"]

shift = 0.4
plt.style.use("dark_background")
figure, axis = plt.subplots(figsize=(9, 9))
labels_before, counts_before = np.unique(before, return_counts=True)
labels_after, counts_after = np.unique(after, return_counts=True)
axis.set_title("Mitral disease stages", fontsize=28, fontweight="bold", c="dimgray")
axis.set_ylabel("amount of people", fontsize=20, fontweight="bold", c="dimgray")

axis.bar(
    np.arange(counts_before.size),
    counts_before,
    width=shift,
    color="cornflowerblue",
    edgecolor="blue",
)

axis.bar(
    np.arange(counts_after.size) + shift,
    counts_after,
    width=shift,
    color="red",
    edgecolor="black",
)

axis.set_xticks(
    (np.arange(labels_before.size) + np.arange(labels_after.size) + shift) / 2,
    labels=labels_after,
    weight="bold",
)

axis.tick_params(axis="x", labelsize=20, labelcolor="dimgray")

plt.show()
