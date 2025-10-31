def count_cycles(arr: list[int]) -> int:
    if not arr:
        return 0
    visited = [False] * len(arr)
    cycle_count = 0
    for i in range(len(arr)):
        if not visited[i]:
            cycle_count += 1
            current = i
            while not visited[current]:
                visited[current] = True
                current = arr[current]
    return cycle_count
