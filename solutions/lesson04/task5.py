def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    N = len(matrix)
    M = len(matrix[0])
    best_row = 0
    current_col = M - 1

    for i in range(N):
        while current_col >= 0 and matrix[i][current_col] == 1:
            best_row = i
            current_col -= 1

    return best_row
