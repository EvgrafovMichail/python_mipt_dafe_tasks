def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    r, c, best = 0, cols - 1, 0
    while r < rows and c >= 0:
        if matrix[r][c] == 1:
            best = r
            c -= 1
        else:
            r += 1
    return best
