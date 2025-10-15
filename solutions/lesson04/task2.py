def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) == 0:
        return []
    intervals.sort()
    res = []
    start, end = intervals[0]
    for i in range(1, len(intervals)):
        if end >= intervals[i][0]:
            end = max(intervals[i][1], end)
        else:
            res.append([start, end])
            start, end = intervals[i]

    res.append([start, end])

    return res
