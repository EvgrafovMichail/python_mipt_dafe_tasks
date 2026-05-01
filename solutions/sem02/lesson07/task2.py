import matplotlib.pyplot as plt


def read_from_json():
    before = {"I": 0, "II": 0, "III": 0, "IV": 0}
    after = {"I": 0, "II": 0, "III": 0, "IV": 0}
    s = 0
    f = open("solutions\sem02\lesson07\data\medic_data.json", "r")
    for line in f.readlines():
        if "before" in line:
            s = 1
        elif "after" in line:
            s = 2
        elif "I" in line:
            if s == 1:
                before[line.split('"')[1]] += 1
            elif s == 2:
                after[line.split('"')[1]] += 1
    f.close()
    return before, after


width = 0.35
before_counts, after_counts = read_from_json()

stages_order = ["I", "II", "III", "IV"]
before_list = [before_counts[stage] for stage in stages_order]
after_list = [after_counts[stage] for stage in stages_order]

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar([i - width / 2 for i in range(4)], before_list, width, label="До", color="skyblue")
ax.bar([i + width / 2 for i in range(4)], after_list, width, label="После", color="lightcoral")

ax.set_xlabel("Степень митральной недостаточности")
ax.set_ylabel("Количество пациентов")
ax.set_title("Распределение пациентов по степеням митральной недостаточности")
ax.set_xticks(range(4))
ax.set_xticklabels(["I", "II", "III", "IV"])
ax.legend()

plt.tight_layout()
plt.savefig("solutions/sem02/lesson07/data/distribution.png", dpi=100)
plt.show()
