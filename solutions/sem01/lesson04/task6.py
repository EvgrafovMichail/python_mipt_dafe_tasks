def count_cycles(arr: list[int]) -> int:
    # ваш код
    n = len(arr)
    cycles = 0

    for i in range(n):
        if arr[i] >= 0:
            cycles += 1
            idx = i
            while arr[idx] >= 0:
                next_idx = arr[idx]
                arr[idx] = -arr[idx] - 1
                idx = next_idx

    return cycles
