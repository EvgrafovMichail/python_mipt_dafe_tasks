def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if intervals == []:
        return []
    intervals.sort()
    ans = []
    for low, r in intervals:
        if [low, r] == intervals[0]:
            ans.append([low, r])
            continue

        l_old, r_old = ans[-1]

        if r_old >= low:
            ans[-1] = [l_old, max(r_old, r)]
        else:
            ans.append([low, r])
    return ans
