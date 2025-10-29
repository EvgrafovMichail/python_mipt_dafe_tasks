def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) <= 1:
        return intervals
    intervals.sort()
    merged_intervals = [intervals[0]]

    for interval in intervals[1:]:
        interval_next = merged_intervals[-1]
        
        if interval[0] <= interval_next[1]:
            interval_next[1] = max(interval_next[1], interval[1])
        else:
            merged_intervals.append(interval)

    return merged_intervals


#print(merge_intervals([[10, 13], [1, 3], [2, 6], [8, 10], [15, 18]]))
#print([[1, 2]])

