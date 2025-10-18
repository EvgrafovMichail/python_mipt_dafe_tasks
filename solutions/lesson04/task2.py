def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    # ваш код
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start < current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    merged.append([current_start, current_end])
    return merged
