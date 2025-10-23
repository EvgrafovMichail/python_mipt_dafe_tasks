def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    maksimum =0
    res =0 
    for i in range(0, len(matrix)):
        if sum(matrix[i]) >maksimum:
            res = i
            maksimum = sum(matrix[i])
    return res