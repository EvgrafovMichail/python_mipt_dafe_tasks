def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    if len(intervals) < 2:
        return intervals

    max_right = 0
    min_left = 10e6
    for i in range(len(intervals)):
        if intervals[i][0] < min_left:
            min_left = intervals[i][0]
        if intervals[i][1] > max_right:
            max_right = intervals[i][1]

    if min_left == 0:
        start_index = -1
    else:
        start_index = min_left
    cnt_intermediate_points = max_right - min_left
    list_of_cnt_restr_in_points = [False] * (max_right - min_left + cnt_intermediate_points + 1)

    for i in range(start_index, max_right + cnt_intermediate_points + 1):
        for j in range(len(intervals)):
            if intervals[j][0] <= i / 2 + 0.5 <= intervals[j][1]:
                list_of_cnt_restr_in_points[i - start_index] = True
    list_of_cnt_restr_in_points.append(False)

    out_list = []
    is_started = False
    for i in range(len(list_of_cnt_restr_in_points)):
        if list_of_cnt_restr_in_points[i] and not is_started:
            start_ind = int((i + 1) / 2 + 0.5)
            is_started = True
        elif not list_of_cnt_restr_in_points[i] and is_started:
            end_ind = int(i / 2 + 0.5)
            if min_left != 0:
                out_list.append([start_ind, end_ind])
            else:
                out_list.append([start_ind - 1, end_ind - 1])
            is_started = False

    return out_list
