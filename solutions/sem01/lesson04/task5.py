def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    maxi = 0
    place = 0
    for i in range(len(matrix)):
        matrix[i].reverse() # на семенаре reverse был
        sumi = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                break
            sumi += 1
        
        if sumi > maxi:
            maxi = sumi
            place = i

    return place
