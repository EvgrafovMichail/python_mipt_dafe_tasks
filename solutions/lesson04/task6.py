def count_cycles(arr: list[int]) -> int: 
    n, masiv, cnt = len(arr), [0]*len(arr), 0
    i = 0
    while i < n:
        if not masiv[i]:
            x = i
            while not masiv[x]:
                masiv[x] = 1
                x = arr[x]
            cnt += 1
        i += 1
    return cnt