def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return 0
    cnt = 1
    row_id = 0
    lm = len(matrix[0])
    for i in range(len(matrix)):
        while matrix[i][-cnt] == 1:
            cnt += 1
            if cnt == lm + 1:
                return i
            row_id = i
    return row_id
