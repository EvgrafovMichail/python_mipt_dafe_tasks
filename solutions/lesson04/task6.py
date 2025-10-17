def count_cycles(arr: list[int]) -> int:
    
    l = len(arr)
    cycle = 0

    for i in range(l):
        if arr[i] >= 0:
            k = i
            while arr[k] >= 0:
                next = arr[k]
                arr[k] = (-1) * l
                k = next
            cycle += 1

    return cycle