def count_cycles(arr: list[int]) -> int:
    mask = [True] * len(arr)
    res = 0
    for i in range(0, len(arr)):
        if mask[i]:
            head = arr[i]
            mask[head] = False
            current = arr[head]
            mask[current] = False
            next = 0
            while head != current:
                next = arr[current]
                mask[current] = False
                current = next
            res += 1
    return res
