def count_cycles(arr: list[int]) -> int:
    len_arr = len(arr)
    if len_arr < 2:
        return len_arr

    arr2 = [1] + [0] * (len_arr - 1)
    cnt_cycles = 0
    end_while = False
    pointer = arr[0]

    while not end_while:
        while arr2[pointer] != 1:
            arr2[pointer] = 1
            pointer = arr[pointer]
        cnt_cycles += 1

        for i in range(len(arr2)):
            if arr2[i] == 0:
                pointer = arr[i]
                break
            if i == len(arr2) - 1:  # для выхода из цикла while
                end_while = True
                break

    return cnt_cycles
