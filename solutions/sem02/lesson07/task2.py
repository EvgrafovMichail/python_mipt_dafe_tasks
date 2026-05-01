import json

import matplotlib.pyplot as plt
import numpy as np


def create_diagram(before: np.ndarray, after: np.ndarray, degree: np.ndarray):
    poses = np.arange(len(degree))
    width = 0.52 / 1.5

    axes = plt.subplots(figsize=(9, 9))[1]
    axes.bar(poses - width / 2, before, width, label="До", color="cornflowerblue", edgecolor="blue")
    axes.bar(poses + width / 2, after, width, label="После", color="indianred", edgecolor="red")
    axes.set_xticks(poses)
    axes.set_xticklabels(degree)
    axes.set_ylabel("Количество пациентов")
    axes.set_title("Степени митральной недостаточности")
    axes.legend()


def create_arrays(path: str) -> tuple[np.ndarray, np.ndarray]:
    with open(path, "r") as f:
        data = json.load(f)

    before = np.array(data["before"])
    after = np.array(data["after"])
    return before, after


def count_degree(arr: np.ndarray, degree: np.ndarray) -> np.ndarray:
    return np.sum(arr[:, None] == degree, axis=0)


def save_diagram(filename: str):
    plt.savefig(filename, dpi=300, bbox_inches="tight")


def main():
    degree = np.array(["I", "II", "III", "IV"])
    before, after = create_arrays("solutions/sem02/lesson07/data/medic_data.json")
    before_count = count_degree(before, degree)
    after_count = count_degree(after, degree)
    create_diagram(before_count, after_count, degree)
    save_diagram("result.png")
    plt.show()


if __name__ == "__main__":
    main()


"""
Выводы:
Ключевые наблюдения:
Тяжёлые стадии (III–IV) заметно уменьшились после имплантации:
III стадия: существенно снизилась
IV стадия: тоже уменьшилась
Лёгкая стадия (I) немного выросла — это положительная динамика.
Однако II стадия резко увеличилась и стала доминирующей после лечения.

Вывод об эффективности импланта:
Имплант в целом оказывает положительный эффект, потому что наблюдается 
явный сдвиг пациентов из тяжёлых состояний (III–IV) в более лёгкие 
(в основном II и частично I стадии).

Но эффект не является полным излечением:
большинство пациентов не переходят в I стадию,
а «улучшение» часто выражается в переходе из тяжёлой стадии в умеренную (II).

Итог:
Имплант эффективен в снижении числа тяжёлых случаев митральной недостаточности, 
но в основном переводит пациентов в среднюю (II) стадию, 
а не в полностью здоровое состояние.
"""
