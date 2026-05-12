# ваш код (используйте функции или классы для решения данной задачи)
import json

import matplotlib.pyplot as plt
import numpy as np


def solve():
    plt.style.use("ggplot")
    info = json.load(open("data/medic_data.json", "r", encoding="utf-8"))
    bef = np.array(info["before"])
    aft = np.array(info["after"])
    levels = ["I", "II", "III", "IV"]
    befc = np.array([np.sum(bef == lev) for lev in levels])
    aftc = np.array([np.sum(aft == lev) for lev in levels])
    f, ax = plt.subplots(figsize=(16, 10))
    x = np.arange(len(levels))
    ax.bar(x - 0.5 / 2, befc, 0.5, label="Before", color="green", edgecolor="black")
    ax.bar(x + 0.5 / 2, aftc, 0.5, label="After", color="blue", edgecolor="black")
    ax.set_title("Mitral disease stages", fontsize=15, fontweight="bold", color="black")
    ax.set_ylabel("Amount of people", fontsize=15, fontweight="bold", color="black")
    ax.set_xticks(x)
    ax.set_xticklabels(levels, fontweight="bold")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    solve()
