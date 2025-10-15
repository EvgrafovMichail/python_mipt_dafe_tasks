def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    ind, mi = 0, float("inf")
    i = 0
    for elem in matrix:
        j = 0
        for num in elem:
            if num:
                if j < mi:
                    mi = j
                    ind = i
                break
            j += 1
        i += 1
    return ind


if __name__ == "__main__":
    print(find_row_with_most_ones([[0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1]]))
    print(find_row_with_most_ones([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
