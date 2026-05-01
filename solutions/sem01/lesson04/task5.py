def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0

    m = len(matrix[0])
    best_index = 0
    for i in range(len(matrix)):
        while m > 0 and matrix[i][m - 1]:
            m -= 1
            best_index = i

    return best_index
