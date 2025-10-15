def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if not intervals:
        return []

    intervals.sort()
    new_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        x1, y1 = new_intervals[-1]
        x2, y2 = intervals[i]
        if x2 <= y1:
            new_intervals[-1] = [x1, max(y2, y1)]
        else:
            new_intervals.append(intervals[i])

    return new_intervals
