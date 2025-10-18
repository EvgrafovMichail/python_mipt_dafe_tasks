def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if not intervals:
        return []

    intervals.sort()
    sublist = intervals[0]
    new_list = []

    for i in range(1, len(intervals)):
        if sublist[1] >= intervals[i][0]:
            sublist = [sublist[0], max(sublist[1], intervals[i][1])]

        else:
            new_list.append(sublist)
            sublist = intervals[i]

    new_list.append(sublist)
    return new_list


list = [[10, 13], [1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(list))
