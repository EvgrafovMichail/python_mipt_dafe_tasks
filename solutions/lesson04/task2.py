def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    intervals = sorted(intervals)
    intervals.append([-2, -1])
    res = []
    for i in range(len(intervals)-1):
        if intervals[i][1]>=intervals[i+1][0] and intervals[i][1]<intervals[i+1][1]:
            intervals[i+1][0] = intervals[i][0]
        
        elif intervals[i][0]<=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]:
            intervals[i+1] = intervals[i]

        else:
            res.append(intervals[i])
    return res
