def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) == 0 or len(intervals) == 1: return intervals
    else:
        i = 0
        while i < len(intervals) -1:
            if intervals[i+1][0] <= intervals[i][1]:
                intervals[i+1][0] = intervals[i][0]
                if intervals[i][1] > intervals[i+1][1]:
                    intervals[i+1][1] = intervals[i][1]
                intervals.pop(i)
            else:
                i+=1
    return intervals