def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if not intervals:
        return []

    n = len(intervals)
    for a in range(n - 1):
        for b in range(a + 1, n):
            if intervals[a][0] > intervals[b][0]:
                intervals[a], intervals[b] = intervals[b], intervals[a]

    result = []
    left = intervals[0][0]
    right = intervals[0][1]

    for i in range(1, n):
        start = intervals[i][0]
        end = intervals[i][1]

        if start <= right:
            if end > right:
                right = end
        else:
            result.append([left, right])
            left = start
            right = end

    result.append([left, right])
    return result
