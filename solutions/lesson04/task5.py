def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if matrix == []:
        return 0
    k = 1
    res = 0
    m = len(matrix[0])
    for i in range(len(matrix)):
        while matrix[i][-k] == 1:
            k += 1
            if k == m + 1:
                return i
            res = i
    return res