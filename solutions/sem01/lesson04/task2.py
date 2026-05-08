def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    intervals.sort(key=lambda x: x[0])
    if len(intervals) == 0:
        return []
    newintervals = []
    start, finish = intervals[0][0], intervals[0][1]
    flag1 = True
    for i in intervals:
        if flag1:
            flag1 = False
            continue  # скип первого элемента(костыль)
        if start < i[0] and finish > i[1]:
            continue
        elif finish >= i[0] and start <= i[0]:
            finish = i[1]
        else:
            newintervals.append([start, finish])
            start = i[0]
            finish = i[1]
    newintervals.append([start, finish])
    return newintervals
