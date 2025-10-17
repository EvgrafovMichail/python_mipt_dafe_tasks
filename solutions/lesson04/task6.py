def count_cycles(arr: list[int]) -> int:
    lengh = len(arr)
    cycle = 0

    for i in range(lengh):
        if arr[i] >= 0:
            k = i
            while arr[k] >= 0:
                next = arr[k]
                arr[k] = (-1) * lengh
                k = next
            cycle += 1

    return cycle
