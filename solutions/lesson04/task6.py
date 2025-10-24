def count_cycles(arr: list[int]) -> int:
    length = len(arr)
    if length == 0:
        return 0
    a = 0
    b = 0
    c = 0

    while b == 0:
        while arr[a] != -1:
            arr[a], a = -1, arr[a]
        c += 1
        b = 1
        for j in range(length):
            if arr[j] > -1:
                a = j
                b = 0
                break
    return c
