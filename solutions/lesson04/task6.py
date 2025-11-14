def count_cycles(arr: list[int]) -> int:
    used_indexes = []
    cycles_count = 0
    for i in range(len(arr)):
        new_index = arr[i]
        f = new_index in used_indexes
        while new_index not in used_indexes:
            used_indexes.append(new_index)
            new_index = arr[new_index]
        if not f:
            cycles_count += 1

    return cycles_count
