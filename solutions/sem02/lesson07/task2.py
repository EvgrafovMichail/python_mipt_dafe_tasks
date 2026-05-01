import json
import os

import matplotlib.pyplot as plt
import numpy as np

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data", "medic_data.json")
with open(file_path, "r") as f:
    data = json.load(f)

plt.style.use("dark_background")
stages = ["I", "II", "III", "IV"]
before_counts = [data["before"].count(s) for s in stages]
after_counts = [data["after"].count(s) for s in stages]

x = np.arange(4)
width = 0.35

plt.bar(x - width / 2, before_counts, width, label="До", color="red")
plt.bar(x + width / 2, after_counts, width, label="После", color="blue")

plt.xlabel("Степень недостаточности")
plt.ylabel("Количество пациентов")
plt.title("Распределение до и после установки импланта")
plt.xticks(x, stages)
plt.legend()

plt.savefig("result.png")
plt.show()
