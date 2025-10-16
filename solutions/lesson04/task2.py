def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) == 0:
        return intervals

    intervals = sorted(intervals)
    length = len(intervals)

    i = 0

    while i != length - 1:
        if intervals[i][1] >= intervals[i + 1][0] and intervals[i][1] < intervals[i + 1][1]:
            intervals.append([intervals[i][0], intervals[i + 1][1]])
            intervals.pop(i)
            intervals.pop(i)
            intervals = sorted(intervals)
            length = len(intervals)
            i = 0
            continue
        elif intervals[i][1] >= intervals[i + 1][1]:
            intervals.pop(i + 1)
            length = len(intervals)
            i = 0
            continue

        i += 1

    return intervals
