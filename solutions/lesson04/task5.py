def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0

    n = len(matrix)
    m = len(matrix[0])

    row, col = 0, m - 1
    best_row = 0

    while row < n and col >= 0:
        if matrix[row][col] == 1:
            best_row = row
            col -= 1  # идём влево, проверяем, не больше ли единиц
        else:
            row += 1  # идём вниз — возможно, у следующего больше единиц

    return best_row
