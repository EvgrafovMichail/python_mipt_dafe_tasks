# %%
import json

import matplotlib.pyplot as plt
import numpy as np


def visualize_medic_data(f_path: str):
    with open(f_path, "r") as f:
        data = json.load(f)

    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(10, 6))

    degrees_of_mitral_regurgitation = ["I", "II", "III", "IV"]

    before_implant_installation = [data["before"].count(i) for i in degrees_of_mitral_regurgitation]
    after_implant_installation = [data["after"].count(i) for i in degrees_of_mitral_regurgitation]

    x = np.arange(len(degrees_of_mitral_regurgitation))

    column1 = ax.bar(
        x - 0.2, before_implant_installation, 0.4, label="До установки импланта", color="#69b3a2"
    )
    column2 = ax.bar(
        x + 0.2, after_implant_installation, 0.4, label="После установки импланта", color="#404080"
    )

    ax.set_title("Эффективность импланта при митральной недостаточности")
    ax.set_ylabel("Количество пациентов")
    ax.set_xticks(x)
    ax.set_xticklabels(degrees_of_mitral_regurgitation)
    ax.legend()

    ax.bar_label(column1)
    ax.bar_label(column2)
    plt.show()


visualize_medic_data("medic_data.json")
# %%
