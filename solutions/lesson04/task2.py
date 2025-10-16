def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    # ваш код

    if len(intervals) <= 1:
        return intervals

    intervals.sort()
    new_intervals = []
    start, end = intervals[0]

    for i in range(1, len(intervals)):
        new_start, new_end = intervals[i]
        if new_start <= end:
            if new_end > end:
                end = new_end
        else:
            new_intervals += [[start, end]]
            start, end = new_start, new_end

    new_intervals += [[start, end]]
    return new_intervals
