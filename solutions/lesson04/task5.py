def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    row = 0
    col = m - 1
    ans = 0
    while row < n and col > -1:
        if matrix[row][col] == 1:
            ans = row
            col -= 1
        else:
            row += 1
    return ans


if __name__ == "__main__":
    print(find_row_with_most_ones([[0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1]]))
    print(find_row_with_most_ones([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
