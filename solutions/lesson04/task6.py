def count_cycles(arr: list[int]) -> int:
    kol = 0
    i = 0
    passed = [0] * len(arr)
    for i in range(len(arr)):
        if passed[i] == 0:
            kol += 1
            curr = i
            while passed[curr] == 0:
                passed[curr] = 1
                curr = arr[curr]
    return kol
