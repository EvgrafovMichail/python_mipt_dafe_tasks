def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    index = maxi =0 
    for i in range(len(matrix)):
        if matrix[i].count(1)>maxi:
            maxi = matrix[i].count(1)
            index = i 
    return index