def find_row_with_most_ones(matrix: list[list[int]]) -> int:
    # ваш код
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])
    best_row = 0
    best_ones = 0

    def first_one(row: list[int]) -> int:
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if row[mid] == 1:
                hi = mid
            else:
                lo = mid + 1
        return lo

    for row_idx in range(n):
        ones = m - first_one(matrix[row_idx])
        if ones > best_ones:
            best_ones = ones
            best_row = row_idx

    return best_row
