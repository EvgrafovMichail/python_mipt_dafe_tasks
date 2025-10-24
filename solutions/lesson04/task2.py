def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) == 0:
        return []

    intervals = sorted(intervals)
    new = []
    curr = intervals[0]

    for i in range(1, len(intervals)):
        nextt = intervals[i]
        if nextt[0] <= curr[1]:
            if nextt[1] > curr[1]:
                curr[1] = nextt[1]

        else:
            new.append(curr)
            curr = nextt

    new.append(curr)
    return new
