def is_arithmetic_progression(lis: list[list[int]]) -> bool:
    if len(lis) < 3: 
        return True
    
    shag = (max(lis) - min(lis)) / (len(lis) - 1)

    if shag == 0:
        return True
    
    if int(shag) != shag: 
        return False
    
    else:
        shag = int(shag)

    newl = list(range(min(lis), max(lis) + 1, shag))
    fl = True

    for x in lis:
        if x not in newl: 
            fl = False

    return fl