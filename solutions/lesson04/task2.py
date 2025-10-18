def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) == 0:
        return intervals
    intervals.sort()
    ans = []
    lt = intervals[0][0]
    rt = intervals[0][1]
    for i in range(len(intervals)):
        if intervals[i][0] <= rt:
            rt = max(intervals[i][1], rt)
        else:
            ans.append([lt, rt])
            lt = intervals[i][0]
            rt = intervals[i][1]
    ans.append([lt, rt])
    return ans
