import matplotlib

matplotlib.use("Agg")
import json

import matplotlib.pyplot as plt
import numpy as np


def get_info(file: str):
    with open(file, "r") as f:
        info = json.load(f)

    before = np.array(info["before"])
    after = np.array(info["after"])
    return before, after


classes = ["I", "II", "III", "IV"]

befor, after = get_info("data/medic_data.json")

sum_befor, sum_after = {}, {}
for class_ in classes:
    sum_befor[class_] = np.sum(befor == class_)
    sum_after[class_] = np.sum(after == class_)


figure, axis = plt.subplots(figsize=(16, 9))
axis: plt.Axes

plt.style.use("ggplot")

x = np.arange(len(classes))
width = 0.4

bar1 = axis.bar(
    x - width / 2, sum_befor.values(), width, label="Before", color="cadetblue", edgecolor="grey"
)

bar2 = axis.bar(
    x + width / 2, sum_after.values(), width, label="After", color="lightcoral", edgecolor="grey"
)

axis.set_title("Mitral disease stages", fontsize=12, fontweight="bold", color="grey")
axis.set_ylabel("amount of people", fontsize=10, fontweight="bold", color="grey")

axis.set_xticks(x)
axis.set_xticklabels(classes, fontweight="bold")


axis.legend()
plt.savefig("medic_info.png")
# plt.show()
