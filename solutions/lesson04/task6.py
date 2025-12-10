def count_cycles(arr: list[int]) -> int:
    k = 0
    for i in range(len(arr)):
        if arr[i] != -1:
            k += 1
        while arr[i] != -1:
            arr[i], i = -1, arr[i]
    return k
