def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    start = 0
    length = len(intervals)
    if length <= 1:
        return intervals

    while start < length - 1:
        union = 0

        for i in range(start + 1, length):
            if max(intervals[start][0], intervals[i][0]) <= min(
                intervals[start][1], intervals[i][1]
            ):
                intervals[start] = [
                    min(intervals[start][0], intervals[i][0]),
                    max(intervals[start][1], intervals[i][1]),
                ]
                intervals.pop(i)
                length -= 1
                union = 1
                break

        if union == 0:
            start += 1
    for i in range(i):
        for j in range(length - i - 1):
            if intervals[j][0] > intervals[j + 1][0]:
                intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]

    return intervals
