def count_cycles(arr: list[int]) -> int:
    summar = 0
    poses = []
    if len(arr) == 0:
        return summar
    for i in range(len(arr)):
        start = arr[i]
        curr = arr[start]
        while curr != start:
            curr = arr[curr]
            poses.append(arr.index(curr))
        if start not in poses:
            summar += 1
            poses.append(curr)
    return summar
