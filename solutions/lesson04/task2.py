def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    intervals.sort()
    ll = []
    if len(intervals) <= 1:
        return intervals
    minc, maxc = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= maxc:
            minc = min(minc, intervals[i-1][0])
            maxc = max(maxc, intervals[i][1])
        else:
            ll.append([minc, maxc])
            minc = intervals[i][0]
            maxc = intervals[i][1]
    maxc = max(maxc, intervals[-1][1])
    ll.append([minc, maxc])
    return ll
print(merge_intervals([[1, 10], [2, 3], [4, 5], [6, 7]]))