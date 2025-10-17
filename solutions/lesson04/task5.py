def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return 0
    cnt = 1
    result = 0
    l = len(matrix[0])
    for i in range(len(matrix)):
        while matrix[i][-cnt] == 1:
            cnt += 1
            if cnt == l + 1:
                return i
            result = i
    return result