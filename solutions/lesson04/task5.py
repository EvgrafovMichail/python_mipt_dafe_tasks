def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    row = 0
    col = len(matrix[0]) - 1
    result_index = 0
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == 1:
            result_index = row
            col -= 1
        else:
            row += 1
    return result_index
