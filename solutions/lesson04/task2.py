def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if not intervals:
        return []
    intervals.sort()
    merged = []
    current_start, current_end = intervals[0]

    for interval in intervals[1:]:
        start, end = interval
        if start <= current_end:
            if end > current_end:
                current_end = end
        else:
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    merged.append([current_start, current_end])
    return merged
