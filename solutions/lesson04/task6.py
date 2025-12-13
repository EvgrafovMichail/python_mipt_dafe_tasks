def count_cycles(arr: list[int]) -> int:
    MAX_s = len(arr)
    for i in range(len(arr)):
        start = arr[i]
        k = start
        counter = 1
        while arr[k] != start:
            counter += 1
            k = arr[k]
        MAX_s = MAX_s - (counter - 1) / counter
    return int(MAX_s)
