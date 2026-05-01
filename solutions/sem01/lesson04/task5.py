def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    row = 0
    line = len(matrix[0]) - 1
    index = 0
    mini_ind = len(matrix[0])

    while row != len(matrix):
        if line == -1:
            return row

        if matrix[row][line] == 0:
            if line < mini_ind:
                mini_ind = line
                index = row

            row += 1

        if row != len(matrix) and matrix[row][line] == 1:
            line -= 1
    return index
