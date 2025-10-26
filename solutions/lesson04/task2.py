def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    arr = []
    for interval in intervals:
        arr.append([interval[0], -1])
        arr.append([interval[1], 1])
    arr.sort()
    cnt_open = 0
    last_begin = 0
    result = []
    for elem in arr:
        cnt_open -= elem[1]
        if cnt_open == 1 and elem[1] == -1:
            last_begin = elem[0]
        elif cnt_open == 0:
            result.append([last_begin, elem[0]])
    return result
