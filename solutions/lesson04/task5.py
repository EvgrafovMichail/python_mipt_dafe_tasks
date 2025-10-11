def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    i = -1
    n = len(matrix)
    if n == 0:
        return 0
    m = len(matrix[0])
    nj = 0
    for j in range(n):
        if matrix[j][i] == 1:
            flag = False
            for ii in range(i, -m - 1, -1):
                if matrix[j][ii] == 0:
                    i = ii
                    nj = j
                    flag = True
                    break
            if not flag:
                return j
    return nj
