def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    better_intervals = sorted(intervals)
    i = 0
    if len(better_intervals) <= 1:
        return better_intervals
    while True:
        first_end = better_intervals[i][-1]
        second_start = better_intervals[i + 1][0]
        if first_end >= second_start:
            if first_end < better_intervals[i + 1][1]:
                better_intervals[i] = [better_intervals[i][0], better_intervals[i + 1][-1]]
                better_intervals.remove(better_intervals[i + 1])
            else:
                better_intervals[i] = [better_intervals[i][0], first_end]
                better_intervals.remove(better_intervals[i + 1])
        else:
            i += 1
        if i >= len(better_intervals) - 1:
            break
    return better_intervals
