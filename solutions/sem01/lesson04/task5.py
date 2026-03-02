def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return 0
    ans = 0
    i = 0
    j = len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == 1:
            ans = i
            j -= 1
        else:
            i += 1
    return ans
