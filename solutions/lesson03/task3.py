def get_nth_digit(num: int) -> int:
    len = 1
    i = 0
    b = 0
    flag = True
    while flag:
        if len == 1:
            count = 5
        else:
            count = 9 * (10 ** (len - 1)) // 2

        cifri = count * len

        if num <= b + cifri:
            mest = num - b
            poz = (mest - 1) // len
            cf = (mest - 1) % len

            if len == 1:
                num = i + 2 * poz
            else:
                perv = 10 ** (len - 1)
                num = perv + 2 * poz

            z = num
            for i in range(len - cf - 1):
                z //= 10
            otv = z % 10
            return otv
            break

        b += cifri
        len += 1
