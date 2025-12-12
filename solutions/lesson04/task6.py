def count_cycles(arr: list[int]) -> int:
    i = 0
    route = 0
    N = len(arr)
    ans = 0
    t = 0
    while i < N:
        if arr[i] >= 0:
            route = i
            while arr[route] >= 0:
                t = arr[route]
                arr[route] = -1
                route = t
            ans += 1
        i += 1
    return ans
