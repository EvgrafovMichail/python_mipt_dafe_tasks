def count_cycles(arr: list[int]) -> int:
    # ваш код
    list_our = set()
    fin = 0
    for i in range(len(arr)):
        if i not in list_our:
            g = i
            while g not in list_our:
                list_our.add(g)
                g = arr[g]
            fin += 1
    return fin
