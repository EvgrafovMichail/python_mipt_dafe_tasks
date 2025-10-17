def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    n = len(matrix)
    m = len(matrix[0])-1
    i = 0
    j = m
    num = 0
    res = 0
    while i != n:
        if matrix[i][j] == matrix[i][j-1] == 1 and j != 0:
            j -= 1
            num = i
        else:
            i += 1
    return num


print(find_row_with_most_ones([[0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))