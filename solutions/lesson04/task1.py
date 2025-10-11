def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    l = lst
    l.sort()
    if len(l) <= 1:
        return True
    c = l[1]-l[0]
    for i in range(2, len(l)):
        if l[i]-l[i-1] != c:
            return False
    return True
print(is_arithmetic_progression([0, 0, 1]))