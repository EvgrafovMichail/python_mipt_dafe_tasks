def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0

    max_count = -1
    result_index = 0
    current_col = len(matrix[0]) - 1  # начинаем с последнего столбца

    for i in range(len(matrix)):
        while current_col >= 0 and matrix[i][current_col] == 1:
            current_col -= 1

        ones_count = len(matrix[0]) - (current_col + 1)

        if ones_count > max_count:
            max_count = ones_count
            result_index = i

    return result_index
