# ваш код (используйте функции или классы для решения данной задачи)
import json

import matplotlib.pyplot as plt
import numpy as np

file_path = "solutions/sem02/lesson07/data/medic_data.json"


def medical_plot_func():
    with open(file_path, "r") as file:
        data = json.load(file)
        before = data["before"]
        after = data["after"]
    before_dist = np.zeros(4, dtype=int)
    after_dist = np.zeros(4, dtype=int)
    for roman in before:
        match roman:
            case "I":
                before_dist[0] += 1
            case "II":
                before_dist[1] += 1
            case "III":
                before_dist[2] += 1
            case "IV":
                before_dist[3] += 1

    for roman in after:
        match roman:
            case "I":
                after_dist[0] += 1
            case "II":
                after_dist[1] += 1
            case "III":
                after_dist[2] += 1
            case "IV":
                after_dist[3] += 1

    degrees = ["I", "II", "III", "IV"]
    x = np.arange(len(degrees))
    width = 0.35

    plt.style.use("ggplot")
    figure, ax = plt.subplots(figsize=(16, 9))
    ax.bar(x - width / 2, before_dist, width, label="До", color="red")
    ax.bar(x + width / 2, after_dist, width, label="После", color="blue")
    ax.set_xticks(x)
    ax.set_xticklabels(degrees)
    ax.legend()

    plt.savefig("distribution.png")
    plt.show()
