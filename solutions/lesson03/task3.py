def get_nth_digit(num: int) -> int:
    if num < 6:
        return (num - 1) * 2

    if num < 96:
        if num % 2 == 0:
            place = num - 5
            num = 10 + ((place - 1) // 2)
            
            if place % 2 == 1:
                return num // 10
            
            else:
                return num % 10
            """
            10 - 1
            18 - 9
            20 - 11
            20 - 12
            22 - 13
            22 - 14
            30 - 21
            """
        else:
            return (num - 5) // 2 + 10
        
    else:
        n = num
        n -= 95
        a = 2
        b = 3

        while n > 0:
            cif = 45 * (10 ** (a - 1)) * (a + 1)

            if n <= cif:
                break

            n -= cif
            a += 1
            b += 1

    past = (n - 1) // b
    place = (n - 1) % b

    first = 10**a
    if first % 2 != 0:
        first += 1

    c = first + past * 2

    for i in range(b - place - 1):
        c //= 10
    return c % 10


"""
    0-8 - 5 1-5 5 цифр 5 чисел
10-98 - 9*5*2 90 цифр 45 чисел 6-95
100-998 - 10*10*5*3 1500 цифр 500 чисел 96-1595 
1000-9998 - 10*10*10*5*4 20000 цифр 5000 чисел 1596-21595
10000-99998 - 10*10*10*10*5*5 250000 цифр, 50000 чисел 21596-71596

если больще 95
ном = 12415
а = 3
б = 2
пока ном больше 0
ном = 45*10**(a-1)*(a+1)
а б += 1
а -= 1
"""
