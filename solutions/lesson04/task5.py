def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    m = len(matrix)

    if m == 0:
        return 0

    n = len(matrix[0])

    answer = 0
    one_pointer = n - 1

    for i in range(0, m):
        if matrix[i][one_pointer] == 0:
            continue

        last_one_pos = one_pointer

        while matrix[i][one_pointer] == 1 and one_pointer >= 0:
            one_pointer -= 1

        if last_one_pos != one_pointer:
            answer = i

    return answer
