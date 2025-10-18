def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0.0
    if n > 0: #определим знак и с помощью этого область, где будем искать
        left = 0.0
        right = max(1.0, n)
    else:
        left = min(-1.0, n)
        right = 0.0

    flag = True

    while flag:
        midle_segmaent = (left + right) / 2.0
        mid_cubed = midle_segmaent * midle_segmaent* midle_segmaent
        
        if abs(mid_cubed - n )<= eps:
            flag = False
        
        if mid_cubed < n:
            left = midle_segmaent
        else:
            right = midle_segmaent
    n = midle_segmaent 
    return n