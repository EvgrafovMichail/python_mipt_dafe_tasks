def count_cycles(arr: list[int]) -> int: 
    if len(arr) == 0:
        return 0
    visited = []
    for i in range(len(arr)):
        visited.append(False)
    cycles = 0
    for i in range(len(arr)):
        if visited[i]:
            continue
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr[j]
        cycles += 1
    return cycles