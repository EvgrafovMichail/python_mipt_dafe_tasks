import json

import matplotlib.pyplot as plt
import numpy as np

STAGES = ("I", "II", "III", "IV")

plt.style.use("ggplot")


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_counts(data: dict):
    before = np.array([data["before"].count(s) for s in STAGES])
    after = np.array([data["after"].count(s) for s in STAGES])
    return before, after


def draw(before: np.ndarray, after: np.ndarray, save_path: str) -> None:
    x = np.arange(len(STAGES))
    width = 0.4

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(x - width / 2, before, width, label="before", color="steelblue")
    ax.bar(x + width / 2, after, width, label="after", color="darkorange")
    ax.set_title("Mitral insufficiency stages", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(STAGES)
    ax.set_ylabel("Number of patients")
    ax.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()


def main():
    data = load_json("data/medic_data.json")
    before, after = build_counts(data)
    draw(before, after, "data/result.png")


if __name__ == "__main__":
    main()
