def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    max_ones = -1
    if len(matrix) == 0:
        return 0
    m = len(matrix[0])
    pos = 0
    i = 0
    for serv in matrix:
        if serv.count(1) > max_ones:
            max_ones = serv.count(1)
            pos = i
        i += 1
        if max_ones == m:
            break
    if max_ones != 0:
        return pos
    else:
        return 0
