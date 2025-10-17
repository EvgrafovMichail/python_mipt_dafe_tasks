def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    maxcount = 0
    res = 0
    j = len(matrix[0]) - 1

    for i in range(len(matrix)):
        while j >= 0 and matrix[i][j] == 1:
            j -= 1

        onescount = len(matrix[0]) - 1 - j

        if onescount > maxcount:
            maxcount = onescount
            res = i

    return res
