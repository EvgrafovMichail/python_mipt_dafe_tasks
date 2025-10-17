def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) == 0:
        return intervals
    intervals.sort()
    m = []
    l = intervals[0][0]
    r = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= r:
            r = max(intervals[i][1], r)
        else:
            m.append([l, r])
            l = intervals[i][0]
            r = intervals[i][1]
    m.append([l, r])
    return m
