def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if intervals == []:
        return []
    intervals.sort()
    result = []
    start = intervals[0][0]
    mx = intervals[0][1]
    for i in range(1, len(intervals)):
        if mx < intervals[i][0]:
            result.append([start, mx])
            start = intervals[i][0]
        mx = max(mx, intervals[i][1])
    result.append([start, mx])
    return result