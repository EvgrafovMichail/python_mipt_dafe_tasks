def count_cycles(arr: list[int]) -> int:
    nc = []
    allnc = []
    c = 0
    for i in range(len(arr)):
        if i in allnc:
            continue
        while i not in nc:
            nc.append(i)
            allnc.append(i)
            i = arr[i]
        nc = []
        c += 1
    return c


print(count_cycles([0]))
