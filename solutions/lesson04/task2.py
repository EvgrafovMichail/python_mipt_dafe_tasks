def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    timeline = []

    for begin, end in intervals:
        timeline.append([begin, "b"])
        timeline.append([end, "e"])

    timeline.sort()
    timeline.append([0, 0])

    interval_counter = 0

    merged_intervals = []
    current_interval = [None, None]

    for i in range(len(timeline) - 1):
        time, mark = timeline[i]
        next_time, _ = timeline[i + 1]

        if mark == "b":
            if interval_counter == 0:
                current_interval[0] = time

            interval_counter += 1

        else:
            interval_counter -= 1

            if interval_counter == 0 and next_time != time:
                current_interval[1] = time
                merged_intervals.append(current_interval.copy())

    return merged_intervals
