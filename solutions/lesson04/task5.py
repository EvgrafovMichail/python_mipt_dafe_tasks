def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    n = len(matrix)
    m = len(matrix[0])
    
    row = 0
    col = m - 1
    result_row = 0
    
    while row < n and col >= 0:
        if matrix[row][col] == 1:
            result_row = row
            col -= 1
        else:
             row += 1
    return result_row