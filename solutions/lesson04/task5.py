def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    
    if len(matrix) == 0:
        return 0
    
    if len(matrix[0]) == 0:
        return 0
    
    max_left_side = 0
    start_list = 0
    countdown = len(matrix[0]) - 1

    while start_list < len(matrix) and countdown >= 0:
        if matrix[start_list][countdown] == 1:
            max_left_side = start_list
            countdown -= 1
        else:
            start_list += 1

    return max_left_side
