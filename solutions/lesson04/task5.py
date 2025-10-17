def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix)
    m = len(matrix[0])
    current_row = 0
    current_col = m - 1
    result = 0

    while current_row < n and current_col >= 0:
        if matrix[current_row][current_col] == 1:
            result = current_row
            current_col -= 1
        else:
            current_row += 1

    return result
