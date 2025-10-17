def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) < 1:
        return []
    else:
        intervals_sort = sorted(intervals)
        noviy_spisok = [intervals_sort[0]]
        for i in range(1, len(intervals_sort)):
            vtoroy_spisok = intervals_sort[i]
            perviy_spisok = noviy_spisok[-1]
            left_2 = vtoroy_spisok[0]
            right_2 = vtoroy_spisok[1]
            right_1 = perviy_spisok[1]
            left_1 = perviy_spisok[0]
            if left_2 <= right_1:
                if right_2 >= right_1:
                    right = right_2
                else:
                    right = right_1
                noviy_spisok[-1] = [left_1, right]
            else:
                noviy_spisok += [vtoroy_spisok]
    return noviy_spisok
