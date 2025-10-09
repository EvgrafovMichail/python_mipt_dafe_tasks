def get_nth_digit(num: int) -> int:
    if num > 5:
        multiplication = 90
        counter = 2
        num2 = num - 5

        while num2 > multiplication:
            counter += 1
            num2 = num2 - multiplication
            multiplication = counter * multiplication * 10 / (counter - 1)

        n = (num2 + num2 % counter) // counter
        res_num = 10 ** (counter - 1) + 2 * (n - 1)
        if num2 % counter != 0:
            res_num = int(res_num // (10 ** (counter - num2 % counter))) % 10
        else:
            res_num = res_num % 10
    else:
        res_num = 2 * (num - 1)

    return res_num
