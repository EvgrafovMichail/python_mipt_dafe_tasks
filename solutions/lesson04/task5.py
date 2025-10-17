def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    # ваш код

    if len(matrix) == 0:
        return 0

    rows_number = len(matrix)
    columns_number = len(matrix[0])
    max_row = -1
    row = 0
    column = columns_number - 1

    while row < rows_number and column >= 0:
        if matrix[row][column] == 0:
            row += 1

        else:
            max_row = row
            column -= 1

    if max_row == -1:
        max_row = 0

    return max_row
