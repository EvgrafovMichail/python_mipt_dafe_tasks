import numpy as np

a = [[True, True], [False, True]]

s = np.where(a)
s_s = np.where(a)[0][0]

print(a)
print(s)
print(s_s)


mins = [True, False, True, False]
maxes = [False, True, False, True]

min_indices = np.where(mins)[0]
s_min_indices = np.where(mins)
print(min_indices)
print(s_min_indices)
