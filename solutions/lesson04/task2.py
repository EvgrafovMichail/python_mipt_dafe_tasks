def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if not intervals:
        return []

    n = len(intervals)
    for i in range(n):
        for j in range(0, n - i - 1):
            if intervals[j][0] > intervals[j + 1][0]:
                intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]

    i = 0
    while i < len(intervals) - 1:
        current = intervals[i]
        next_interval = intervals[i + 1]

        if current[1] >= next_interval[0]:
            intervals[i][1] = max(current[1], next_interval[1])
            intervals.pop(i + 1)
        else:
            i += 1

    return intervals
