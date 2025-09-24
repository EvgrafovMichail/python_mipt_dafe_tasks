def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0
    # ваш код
    while (num != 1):
        if num % 2 != 0:
            multiplications_amount += 2
            num = (num - 1) / 2

        else:
            multiplications_amount += 1
            num = num / 2


    return multiplications_amount
