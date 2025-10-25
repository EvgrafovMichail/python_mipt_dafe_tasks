def count_cycles(arr: list[int]) -> int:
    visited = [0] * len(arr)
    cycles = 0
    for i in range(len(arr)):
        if not visited[i]:
            curr = i
            while not visited[curr]:
                visited[curr] = 1
                curr = arr[curr]
            cycles += 1
    return cycles
