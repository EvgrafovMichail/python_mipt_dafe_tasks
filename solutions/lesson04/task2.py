def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    # ваш код
    if not intervals:
        return []
    intervals.sort(key=lambda p: p[0])
    merged = []
    cur_left, cur_right = intervals[0]
    for left, right in intervals[1:]:
        if left <= cur_right + 1:
            cur_right = max(cur_right, right)
        else:
            merged.append((cur_left, cur_right))
            cur_left, cur_right = left, right
    merged.append((cur_left, cur_right))