def count_cycles(arr: list[int]) -> int:
    visited = [False] * len(arr)
    count = 0

    pointer = 0

    while pointer < len(arr):
        if visited[pointer]:
            pointer += 1
            continue

        visited[pointer] = True
        pointer = arr[pointer]

        count += 1
        while not visited[pointer]:
            visited[pointer] = True
            pointer = arr[pointer]

        pointer += 1

    return count
