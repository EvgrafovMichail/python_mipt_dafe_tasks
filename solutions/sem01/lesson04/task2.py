def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) == 0:
        return []
    intervals = sorted(intervals)
    i = 0
    while i != len(intervals) - 1:
        if intervals[i][1] >= intervals[i + 1][0]:
            if intervals[i][1] <= intervals[i + 1][1]:
                intervals[i] = [intervals[i][0], intervals[i + 1][1]]
                intervals.pop(i + 1)
            else:
                intervals.pop(i + 1)
        else:
            i += 1
    return intervals
