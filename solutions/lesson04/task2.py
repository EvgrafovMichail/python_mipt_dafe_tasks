def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if intervals == []:
        return []
    temp = 0
    for i in range(0, len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i][0] > intervals[j][0]:
                temp = intervals[i]
                intervals[i] = intervals[j]
                intervals[j] = temp

    ans = [intervals[0]]

    for i in intervals[1:]:
        if i[0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], i[1])
        else:
            ans.append(i)
    return ans