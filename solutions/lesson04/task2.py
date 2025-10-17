def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    # ваш код
    if intervals == []:
        return []
    for i in range(0, len(intervals)):
        for g in range(i + 1, len(intervals)):
            if intervals[i][0] > intervals[g][0]:
                intervals[i], intervals[g] = intervals[g], intervals[i]
    fin = [intervals[0]]
    for i in intervals[1:]:
        if i[0] <= fin[-1][1]:
            fin[-1][1] = max(fin[-1][1], i[1])
        else:
            fin.append(i)

    return fin
