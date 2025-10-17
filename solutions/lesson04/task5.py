def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    i = 0
    j = 0
    N = len(matrix)
    if N != 0:
        M = len(matrix[0])
    else:
        return 0

    while j < M:
        while i < N:
            if matrix[i][j] == 1:
                return i
            i += 1
        i = 0
        j += 1
    return 0
