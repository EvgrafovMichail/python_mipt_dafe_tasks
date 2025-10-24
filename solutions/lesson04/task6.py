def count_cycles(arr: list[int]) -> int:
    count = 0

    for i in range(len(arr)):
        if arr[i] == -1:
            continue

        next = i

        while arr[next] != -1:
            prev = arr[next]
            arr[next] = -1

            next = prev

        arr[next] = -1

        count += 1

    return count
