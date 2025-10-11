def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    intervals.sort()
    l = []
    if len(intervals) <= 1:
        return intervals
    minc, maxc = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= maxc:
            minc = min(minc, intervals[i-1][0])
            maxc = max(maxc, intervals[i][1])
        else:
            l.append([minc, maxc])
            minc = intervals[i][0]
            maxc = intervals[i][1]
    maxc = max(maxc, intervals[-1][1])
    l.append([minc, maxc])
    return l
print(merge_intervals([[1, 10], [2, 3], [4, 5], [6, 7]]))