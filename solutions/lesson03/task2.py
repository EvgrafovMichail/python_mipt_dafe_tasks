def get_cube_root(n: float, eps: float) -> float:
    if n == 1:
        return 1.0
    
    if n == -1:
        return -1.0

    if abs(n) > 1:
        if n > 0:
            x3max = n
            x3min = 1

        else:
            x3max = -1
            x3min = n

        x3 = (x3max + x3min) / 2.0
        while abs(n - x3 * x3 * x3) > eps:
            if x3 * x3 * x3 > n:
                x3max = x3
                x3 = (x3max + x3min) / 2.0

            else:
                x3min = x3
                x3 = (x3max + x3min) / 2.0

        return x3

    if abs(n) < 1:
        if n == 0:
            return 0
        
        else:
            if n > 0:
                x3max = 1
                x3min = 0

            else:
                x3max = 0
                x3min = -1
            x3 = (x3max + x3min) / 2.0

            while abs(n - x3 * x3 * x3) > eps:
                if x3 * x3 * x3 > n:
                    x3max = x3
                    x3 = (x3max + x3min) / 2.
                    
                else:
                    x3min = x3
                    x3 = (x3max + x3min) / 2.0

            return x3
