# ваш код (используйте функции или классы для решения данной задачи)
import json

import matplotlib.pyplot as plt
import numpy as np

with open(
    "C:\projects\python_git\git_python_sem_2\python_mipt_dafe_tasks\solutions\sem02\lesson07\data\medic_data.json",
    "r",
    encoding="utf-8",
) as file:
    data = json.load(file)

before = data["before"]
after = data["after"]

degrees = ["I", "II", "III", "IV"]
before_counts = {d: 0 for d in degrees}
after_counts = {d: 0 for d in degrees}


for degree in before:
    before_counts[degree] += 1

for degree in after:
    after_counts[degree] += 1

x = np.arange(len(degrees))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x - width / 2, before_counts.values(), width, label="До импланта", color="hotpink")

ax.bar(x + width / 2, after_counts.values(), width, label="После импланта", color="lightpink")


ax.set_xlabel("Степень митральной недостаточности")
ax.set_ylabel("Количество пациентов")
ax.set_title("Распределение пациентов по степеням")
ax.set_xticks(x)
ax.set_xticklabels(degrees)
ax.legend()


plt.savefig("heart_implant_analysis.png", bbox_inches="tight")
plt.show()
