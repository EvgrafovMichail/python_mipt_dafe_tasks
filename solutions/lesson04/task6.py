def count_cycles(arr: list[int]) -> int:
    visited = [0] * len(arr)
    count = 0
    for i in range(len(arr)):
        if not visited[i]:
            count += 1
            current = i
            while not visited[current]:
                visited[current] = 1
                current = arr[current]
    return count
