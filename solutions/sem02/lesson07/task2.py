import matplotlib.pyplot as plt
import numpy as np

before = [0]*4
after = [0]*4
file_path = 'D:/GitHub/python_mipt_dafe_tasks/solutions/sem02/lesson07/data/medic_data.json'
with open(file_path, 'r') as file:
    content = file.read()

before_part = content.split('"before"')[1].split('"after"')[0]
after_part = content.split('"after"')[1]

before[0] = before_part.count('"I"') - before_part.count('"IV"')
before[1] = before_part.count('"II"')
before[2] = before_part.count('"III"')
before[3] = before_part.count('"IV"')

after[0] = after_part.count('"I"') - after_part.count('"IV"')
after[1] = after_part.count('"II"')
after[2] = after_part.count('"III"')
after[3] = after_part.count('"IV"')

figure, axis = plt.subplots(figsize=(9, 9))

stages = np.array(['I', 'II', 'III', 'IV'])
axis.set_xticks(np.arange(stages.size), labels=stages, weight="bold")

x = np.arange(4)
width = 0.35

axis.bar(x - width/2, before, width, color='goldenrod', edgecolor='brown')
axis.bar(x + width/2, after, width, color='lightgreen', edgecolor='olive')

axis.set_ylabel('amount of people')
axis.set_title('Mitral desease stages')
axis.legend(["before", "after"], title="Desease stages")

figure.savefig("medic.png", bbox_inches="tight")
plt.show()


