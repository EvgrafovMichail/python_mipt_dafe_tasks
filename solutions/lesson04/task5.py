def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    # ваш код
    if not matrix:
        return 0
    max = -1  
    result_index = 0 
    column = len(matrix[0]) - 1 
    for i in range(len(matrix)):
        while column >= 0 and matrix[i][column] == 1:
            column -= 1
        num_ones = len(matrix[0]) - (column + 1)
        if num_ones > max:
            max = num_ones
            result_index = i
    
    return result_index
