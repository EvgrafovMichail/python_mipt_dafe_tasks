def merge_intervals(intervals: list[list[int]]) -> list[list[int, int]]:
    d = [False] * 24
    for elem in intervals:
        for i in range(elem[0], elem[1]):
            d[i] = True
    k, a = list(), -1
    for i in range(len(d)):
        if d[i] and a == -1:
            a = i
        elif a != -1 and not d[i]:
            k.append([a, i])
            a = -1
    return k
