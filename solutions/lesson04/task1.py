def is_arithmetic_progression(l: list[list[int]]) -> bool:
    if len(l) < 3:
        return True
    shag = (max(l) - min(l)) / (len(l) - 1)
    if shag == 0:
        return True
    if int(shag) != shag:
        return False
    else:
        shag = int(shag)
    newl = list(range(min(l), max(l) + 1, shag))
    fl = True
    for x in l:
        if x not in newl:
            fl = False
    return fl


print(is_arithmetic_progression([1, 1, 1, 1]))
