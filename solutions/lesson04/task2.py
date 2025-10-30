def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) == 0:
        return intervals
    intervals.sort()
    m = []
    left = intervals[0][0]
    right = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= right:
            right = max(intervals[i][1], right)
        else:
            m.append([left, right])
            left = intervals[i][0]
            right = intervals[i][1]
    m.append([left, right])
    return m
