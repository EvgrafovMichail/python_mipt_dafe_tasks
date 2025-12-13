def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return 0

    y = len(matrix[0]) - 1
    index_max = 0

    for x in range(len(matrix)):
        while y >= 0 and matrix[x][y] == 1:
            index_max = x
            y -= 1

    return index_max
