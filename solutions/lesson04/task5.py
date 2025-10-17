def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    length = len(matrix)
    if length < 1:
        return 0
    m = 0
    i = 0
    j = len(matrix[0]) - 1

    while i < length and j > -1:
        if matrix[i][j] == 1:
            j -= 1
            m = i
        else:
            i += 1

    return m
