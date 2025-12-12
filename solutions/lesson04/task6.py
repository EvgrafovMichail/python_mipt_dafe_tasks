def count_cycles(arr: list[int]) -> int:
    n = len(arr)
    cicle_nums = 0
    ans = 0
    for i in range(n):
        if cicle_nums & (1 << i) == 0:
            ans += 1
            begin = i
            cicle_nums += 1 << i
            head = arr[i]
            while head != begin:
                cicle_nums += 1 << head
                head = arr[head]

    return ans
