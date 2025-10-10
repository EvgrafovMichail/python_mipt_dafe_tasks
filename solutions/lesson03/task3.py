def get_nth_digit(num: int) -> int:
    t = 0
    s = 1
    if num == 1:
        return 0
    
    while True :
        t += 2
        T = t
        sT = 0

        while T > 0:
            T = T//10
            sT += 1

        s += sT

        if s >= num :
            r = sT
            break

    a = t//(10 ** (s - num))
    print(t, r, num, s)
    return a%10



print(get_nth_digit(5))

