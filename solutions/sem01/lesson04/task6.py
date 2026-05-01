def count_cycles(arr: list[int]) -> int:
    length = len(arr)
    if length == 0:
        return 0
    a, f, k = 0, 0, 0

    while f == 0:
        while arr[a] != -1:
            arr[a], a = -1, arr[a]
        k += 1
        f = 1
        for j in range(length):
            if arr[j] > -1:
                a = j
                f = 0
                break
    return k
