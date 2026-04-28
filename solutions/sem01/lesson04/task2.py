def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    intervals.sort()
    new_intervals = []

    if len(intervals) > 0:
        left = intervals[0][0]
        right = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][1] > right:
                if intervals[i][0] > right:
                    new_intervals.append([left, right])
                    left = intervals[i][0]

                right = intervals[i][1]

        new_intervals.append([left, right])

    return new_intervals
