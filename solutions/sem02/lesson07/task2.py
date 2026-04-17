import json

import matplotlib.pyplot as plt
import numpy as np


def load_from_json(path):
    with open(path, "r") as file:
        loaded_data = json.load(file)

    before = np.array(loaded_data["before"])
    after = np.array(loaded_data["after"])

    return before, after


def counting_stages(data, stages):
    before, after = data

    cnt_before = np.array([np.sum(before == stage) for stage in stages])
    cnt_after = np.array([np.sum(after == stage) for stage in stages])

    return cnt_before, cnt_after


def make_label(axis):
    axis.set_ylabel("amount of people")
    axis.set_title("Mitral disease stages")
    axis.legend()


def visualize_bar(counts, stages):
    figure, axis = plt.subplots(figsize=(7, 7))

    cnt_before, cnt_after = counts

    ordinates = np.arange(cnt_before.size)

    axis.set_xticks(ordinates)
    axis.set_xticklabels(stages)

    width = 0.4

    axis.bar(ordinates - width / 2, cnt_before, color="blue", width=width, label="before")

    axis.bar(ordinates + width / 2, cnt_after, color="red", width=width, label="after")

    make_label(axis)

    return figure


if __name__ == "__main__":
    abs_path = "solutions/sem02/lesson07/"

    plt.style.use("bmh")

    stages = ("I", "II", "III", "IV")

    data = load_from_json(abs_path + "data/medic_data.json")

    counts = counting_stages(data, stages)

    figure = visualize_bar(counts, stages)

    figure.savefig(abs_path + "bar.png")

    plt.show()


# На графике видно улучшения состояние пациентов:
#     людей с третьей и четвертой стадией стало меньше,
#     они частично выличились, что привело к увеличению
#     количества людей со второй стадией

# Вывод имплант эффективен
