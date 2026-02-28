def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    if matrix == []:
        return 0

    max_one = 0
    index = 0

    for i in range(len(matrix)):
        sub_matrix = matrix[i]
        count_one = 0

        for j in range(len(sub_matrix) - 1, -1, -1):
            if sub_matrix[j] == 1:
                count_one += 1
            else:
                break

        if count_one > max_one:
            max_one = count_one
            index = i
    return index
