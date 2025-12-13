def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) == 0:
        return []
    intervals.sort()
    new_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        now = intervals[i]
        previos = new_intervals[-1]
        if now[0] <= previos[1]:
            if now[1] > previos[1]:
                previos[1] = now[1]
        else:
            new_intervals.append(now)

    return new_intervals
