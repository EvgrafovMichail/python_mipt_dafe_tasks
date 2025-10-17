def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    length = len(matrix)
    if length < 1:
        return 0
    n = 0
    i, j = 0, len(matrix[0]) - 1
    while i < length and j > -1:
        if matrix[i][j] == 1:
            j -= 1
            n = i
        else:
            i += 1

    return n
