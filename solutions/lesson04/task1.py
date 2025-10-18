def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst.sort()
    len_lst = len(lst)
    
    if len_lst <= 1:
        return True
    
    b = lst[1] - lst[0]
    for i in range(2, len_lst):
        if lst[i] - lst[i-1] != b:
            return False
    return True

#print(is_arithmetic_progression([]))