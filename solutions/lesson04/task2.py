def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals):
        intervals.sort()

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i : i + 2] = [
                    [intervals[i][0], max(intervals[i + 1][1], intervals[i][1])]
                ]

            else:
                i += 1

        return intervals

    return []
