def get_cube_root(n: float, eps: float) -> float:
    if n == 0 or n == 1 or n == -1:
        return n
    else:
        if abs(n)<1:   #устанавливаем значения top. С учётом значения n (небольшая оптимизация. не считаем лишнее)
            top = 1
        elif abs(n)<3:
            top = abs(n)
        else:
            top = abs(n)/2
        bottom = 0
        x=abs(n)
        while abs((x**3 - abs(n))) > eps:
            x=(top+bottom)/2
            if x**3 > abs(n):
                top = x
            else:
                bottom = x
        if n > 0:
            return x
        else:
            return -x


                         
            

   