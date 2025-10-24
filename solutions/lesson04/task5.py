def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    maxsum = 0
    num = 0
    for i in range(len(matrix)):
        if sum(matrix[i]) == len(matrix[i]):
            return i
        if sum(matrix[i]) > maxsum:
            maxsum = sum(matrix[i])
            num = i
    return num
