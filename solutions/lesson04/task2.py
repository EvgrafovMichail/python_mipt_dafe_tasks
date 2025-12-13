def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    intervals.sort()

    time = []

    for left, right in intervals:
        if not time or left > time[-1][1]:
            time.append([left, right])
        else:
            time[-1][1] = max(time[-1][1], right)

    return time
