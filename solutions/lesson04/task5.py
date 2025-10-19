def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n > 0:
        m = len(matrix[0])
        num_with_max = 0
        final = m - 1
        for i in range(n):
            while final >= 0 and matrix[i][final] == 1:
                final -= 1
                num_with_max = i

        return num_with_max
    return 0
