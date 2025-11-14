def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    max_row = 0
    j = m - 1
    for i in range(n):
        while j >= 0 and matrix[i][j] == 1:
            j -= 1
            max_row = i
    return max_row
