def count_cycles(arr: list[int]) -> int:
    k = 0
    for i in range(len(arr)):
        ind, elem = i, 0
        while ind != i or elem == 0:
            ind = arr[ind]
            elem += 1
        k += 1 / elem
    return round(k)
