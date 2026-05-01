def count_cycles(arr: list[int]) -> int:
    counter = 0
    visited = [False] * len(arr)
    while not all(visited):
        start = visited.index(False)
        i = start
        visited[start] = True
        while arr[i] != start:
            visited[arr[i]] = True
            i = arr[i]
        counter += 1
    return counter
