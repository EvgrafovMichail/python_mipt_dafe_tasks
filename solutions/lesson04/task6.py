def count_cycles(arr: list[int]) -> int:
    n = len(arr)
    visited = [False] * n
    result = 0

    for i in range(n):
        if not visited[i]:
            result += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j]

    return result
