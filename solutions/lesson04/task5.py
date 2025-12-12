def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return 0

    n = len(matrix[0]) - 1
    good_row = 0

    for m in range(len(matrix)):
        while n >= 0:
            if matrix[m][n] == 0:
                break
            n -= 1
            good_row = m

    return good_row
