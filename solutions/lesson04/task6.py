def count_cycles(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0

    cycles = 0
    passed = []

    for start_index in range(len(arr)):
        if start_index not in passed:
            cycles += 1
            current_index = start_index
            while current_index not in passed:
                passed.append(current_index)
                current_index = arr[current_index]

    return cycles
