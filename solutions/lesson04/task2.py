def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    intervals.sort()

    res = []
    i = 0
    while i < len(intervals):
        start = intervals[i][0]
        end = intervals[i][1]
        while i < len(intervals) - 1 and intervals[i+1][0] <= end <= intervals[i+1][1]:
            end = intervals[i+1][1]
            i += 1
        i += 1
        if len(res) == 0 or res[-1][1] < end:
            res.append([start, end])

    return res