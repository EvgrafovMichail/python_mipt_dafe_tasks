def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return 0

    new = sorted(matrix)

    for i in range(len(matrix)):
        if matrix[i] == new[len(new) - 1]:
            return i
