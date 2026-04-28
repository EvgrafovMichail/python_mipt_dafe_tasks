def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    n, m = len(matrix), len(matrix[0])
    i = 0
    j = m - 1
    index = 0
    while j >= 0 and i < n:
        if matrix[i][j] == 1:
            index = i
            j -= 1
        else:
            i += 1
    return index
