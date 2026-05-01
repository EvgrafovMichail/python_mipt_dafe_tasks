import json
import os

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

STAGES = ["I", "II", "III", "IV"]
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "medic_data.json")


def load_data(path):
    with open(path, "r") as f:
        return json.load(f)


def count_stages(vals):
    return [vals.count(s) for s in STAGES]


def plot_and_save(before, after, path):
    x = np.arange(len(STAGES))
    w = 0.35

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.bar(
        x - w / 2,
        before,
        w,
        label="до",
        color="cornflowerblue",
    )
    ax.bar(
        x + w / 2,
        after,
        w,
        label="после",
        color="sandybrown",
    )

    ax.set_title(
        "Стадии митральной недостаточности",
        fontsize=17,
        fontweight="bold",
        color="dimgray",
    )
    ax.set_ylabel(
        "количество пациентов",
        fontsize=14,
        fontweight="bold",
        color="dimgray",
    )
    ax.set_xticks(x, labels=STAGES)
    ax.tick_params(
        axis="x",
        labelsize=14,
        labelcolor="dimgray",
    )
    ax.legend(fontsize=13)

    plt.savefig(path)


def main():
    data = load_data(DATA_PATH)
    before = count_stages(data["before"])
    after = count_stages(data["after"])
    plot_and_save(before, after, "task2.png")


if __name__ == "__main__":
    main()
# Я нашел в интернете модуль os, надеюсь его можно было использовать
# Иначе на другом устройстве не работало бы, если бы я оставил путь
# для своей файловой системы
# Судя по графику имплан эффективен, ведь после его установки количество
# пациентов с высокой стадией уменьшилось (а с малой стадией увеличилось)
