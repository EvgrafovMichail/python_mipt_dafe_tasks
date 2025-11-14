def get_multiplications_amount(num: int) -> int:
    n = num
    multiplications_amount = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            multiplications_amount += 1
        else:
            n -= 1
            multiplications_amount += 1

    return multiplications_amount
