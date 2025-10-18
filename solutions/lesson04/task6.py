def count_cycles(arr: list[int]) -> int:
    cnt = 0
    mas = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        while mas[arr[i]] != 1:
            mas[i], i = 1, arr[i]
        cnt += 1
        mas = [0 for i in range(len(arr))]
    return cnt
