def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if not intervals:
        return []

    intervals.sort() 
    
    res = []
    i_interval = intervals[0]
    
    for i in range(1, len(intervals)):
        if i_interval [1] >=  intervals[i][0] :
            i_interval[1] = max(i_interval[1],  intervals[i][1])
        else:
            res.append(i_interval)
            i_interval =  intervals[i]

    res.append(i_interval)
    
    return res
    
    
    