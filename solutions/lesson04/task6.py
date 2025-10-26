def count_cycles(arr: list[int]) -> int:
    cnt_cycles = 0
    used = [False] * len(arr)
    for i in range(len(arr)):
        if not used[i]:
            cnt_cycles += 1
            used[i] = True
            while not used[arr[i]]:
                i = arr[i]
                used[i] = True
    return cnt_cycles
