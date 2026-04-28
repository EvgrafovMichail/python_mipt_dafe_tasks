# ваш код (используйте функции или классы для решения данной задачи)


import json

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")


def build_diagrams(data: dict[str : list[str]]) -> None:
    figure = plt.figure(figsize=(20, 10))
    axis = figure.add_subplot(1, 1, 1)

    counts_before = np.array([0] * 4)
    for i in range(len(data["before"])):
        counts_before[0] += data["before"][i] == "I"
        counts_before[1] += data["before"][i] == "II"
        counts_before[2] += data["before"][i] == "III"
        counts_before[3] += data["before"][i] == "IV"

    counts_after = np.array([0] * 4)
    for i in range(len(data["after"])):
        counts_after[0] += data["after"][i] == "I"
        counts_after[1] += data["after"][i] == "II"
        counts_after[2] += data["after"][i] == "III"
        counts_after[3] += data["after"][i] == "IV"

    axis.set_title("Mitral disease stages", fontsize=17, fontweight="bold", c="#86CFFF")
    axis.set_ylabel("amount of people", fontsize=14, fontweight="bold", c="#86CFFF")
    axis.set_xticks(
        np.arange(4),
        labels=["I", "II", "III", "IV"],
        weight="bold",
        fontsize=17,
    )

    axis.bar(
        np.arange(4) - 0.15,
        np.array(counts_before),
        label="before",
        color="#0090B4",
        edgecolor="#86CFFF",
        width=0.3,
    )

    axis.bar(
        np.arange(4) + 0.15,
        np.array(counts_after),
        label="after",
        color="#B40000",
        edgecolor="#FF8686",
        width=0.3,
    )

    axis.legend(fontsize=17, labelcolor="#86CFFF")


if __name__ == "__main__":
    with open("medic_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    build_diagrams(data)
    plt.show()
