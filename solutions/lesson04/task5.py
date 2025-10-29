def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    len_matrix = len(matrix)
    if len_matrix <= 1:
        return 0
    
    len_first = len(matrix[0])
    if len_first <=1:
        return 0
    
    server = 0
    best_s = 0
    work = len_first - 1
    
    while server < len_matrix and work >= 0:
        if matrix[server][work] == 1:
            best_s = server
            work = work - 1
        else:
            server += 1
    return best_s


#print(find_row_with_most_ones([[0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1]]))
#print(find_row_with_most_ones([[0, 1]]))
#print(find_row_with_most_ones([]))