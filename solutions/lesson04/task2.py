def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if not intervals:
        return []

    intervals.sort()

    merged = []
    current_start, current_end = intervals[0]

    for i in range(1, len(intervals)):
        next_start, next_end = intervals[i]

        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = next_start, next_end

    merged.append([current_start, current_end])

    return merged
