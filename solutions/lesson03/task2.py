def get_cube_root(n: float, eps: float) -> float:
    if n > 1:
        left_end, right_end = 0, n
    elif 0 <= n <= 1:
        left_end, right_end = 0, 1
    else: 
        left_end, right_end = n, 0

    while True:
        middel = (left_end + right_end) / 2
        cube = middel * middel * middel
        delta = abs(cube - n)

        if delta <= eps:
            return middel
        elif cube < n:
            left_end = middel
        else:
            right_end = middel
