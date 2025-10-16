def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    # ваш код
    if not intervals:
        return []
    intervals.sort(key=lambda p: p[0])
    merged = []
    cur_l, cur_r = intervals[0]
    for l, r in intervals[1:]:
        if l < cur_r + 1:
            cur_r = max(cur_r, r)
        else:
            merged.append([cur_l, cur_r])
            cur_l, cur_r = l, r
    merged.append([cur_l, cur_r])
    return merged
