def count_cycles(arr: list[int]) -> int:
    count = 0
    visited = [False] * len(arr)

    for i in range(len(arr)):
        if visited[i]:
            continue

        index = i
        count += 1
        while not visited[index]:
            visited[index] = True
            index = arr[index]

    return count
