# ваш код (используйте функции или классы для решения данной задачи)
import json
from typing import Dict, Final, Tuple

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")

arabic_to_roman: Final[Dict[int, str]] = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
}


class PlotConfig:
    STAGES_AMOUNT: Final[int] = 4
    BAR_WIDTH: Final[float] = 0.35

    class Colors:
        before: Final[str] = "#7FA6B5"
        after: Final[str] = "#BFAB95"
        before_edge: Final[str] = "#647075"
        after_edge: Final[str] = "#4B4033"

    class Fonts:
        labels: Final[dict] = {"fontsize": 17, "fontweight": "bold", "color": "dimgray"}
        titles: Final[dict] = {"fontsize": 23, "fontweight": "bold", "color": "dimgray"}
        legend: Final[dict] = {
            "fontsize": 20,
        }


def load_data(path_to_file: str) -> Tuple[np.ndarray, np.ndarray]:
    patients_stages_before = np.zeros(PlotConfig.STAGES_AMOUNT, dtype=np.uint64)
    patients_stages_after = np.zeros(PlotConfig.STAGES_AMOUNT, dtype=np.uint64)

    with open(path_to_file) as file:
        data = json.load(file)

        for degree in range(PlotConfig.STAGES_AMOUNT):
            patients_stages_before[degree] = data["before"].count(arabic_to_roman[degree + 1])
            patients_stages_after[degree] = data["after"].count(arabic_to_roman[degree + 1])

    return patients_stages_before, patients_stages_after


def create_diagram(path_to_file: str, file_name: str, width: int, height: int, dpi: int) -> None:
    if not path_to_file or not file_name:
        raise ValueError

    if width < 0 or height < 0 or dpi < 0:
        raise ValueError

    patients_stages_before, patients_stages_after = load_data(path_to_file)

    x_ticks = np.arange(PlotConfig.STAGES_AMOUNT)

    figure, axis = plt.subplots(figsize=(width, height))

    axis.bar(
        np.arange(patients_stages_before.size) - PlotConfig.BAR_WIDTH / 2,
        patients_stages_before,
        label="before",
        width=PlotConfig.BAR_WIDTH,
        color=PlotConfig.Colors.before,
        edgecolor=PlotConfig.Colors.before_edge,
    )
    axis.bar(
        np.arange(patients_stages_after.size) + PlotConfig.BAR_WIDTH / 2,
        patients_stages_after,
        label="after",
        width=PlotConfig.BAR_WIDTH,
        color=PlotConfig.Colors.after,
        edgecolor=PlotConfig.Colors.after_edge,
    )

    axis.set_title("Mitral disease stages", **PlotConfig.Fonts.titles)
    axis.set_ylabel("amount of people", **PlotConfig.Fonts.labels)

    axis.set_xticks(x_ticks)
    axis.set_xticklabels(
        [arabic_to_roman[i + 1] for i in range(PlotConfig.STAGES_AMOUNT)], **PlotConfig.Fonts.labels
    )

    axis.legend(**PlotConfig.Fonts.legend)

    figure.savefig(file_name, bbox_inches="tight", dpi=dpi)


if __name__ == "__main__":
    create_diagram("data/medic_data.json", "medic_data_diag", 16, 9, 300)
