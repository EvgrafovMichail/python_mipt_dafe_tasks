def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    
    a = len(matrix)
    b = len(matrix[0])
    
    i = b
    j = 1
    n = 0
    while j <= a and i > 0:
        if matrix[j - 1][i - 1] == 1:
            i -= 1
            n = j
        else :
            j += 1

    if n == 0:
        return 0
    
    return n - 1


matrix= []
print(find_row_with_most_ones(matrix))