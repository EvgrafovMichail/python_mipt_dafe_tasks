def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst_sort = sorted(lst)
    if (len(lst_sort) <=2):
        return True
    
    diffrence = lst_sort[1]-lst_sort[0]

    for i in range(len(lst_sort)-1):
        if lst_sort[i+1]-lst_sort[i]!=diffrence:
            return False
    
    return True