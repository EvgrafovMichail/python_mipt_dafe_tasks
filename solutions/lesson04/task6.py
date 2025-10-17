def count_cycles(arr: list[int]) -> int:
    # ваш код

    if len(arr) == 0:
        return 0

    start_index, index = 0, 0
    cycle_count = 0
    while cycle_count == 0:
        if arr[index] != 0:
            start_index = index
            index = arr[index]
            arr[start_index] = 0
        else:
            cycle_count = 1

    for index in range(1, len(arr)):
        if arr[index] == 0:
            continue
        else:
            while arr[index] != 0:
                start_index = index
                index = arr[index]
                arr[start_index] = 0
            cycle_count += 1

    return cycle_count
