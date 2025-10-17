def count_cycles(arr: list[int]) -> int:
    see, ans = set(), 0
    for i in range(len(arr)):
        if i not in see:
            j = i
            while j not in see:
                see.add(j)
                j = arr[j]
            ans += 1
    return ans
