def get_nth_digit(n: int) -> int:
    #  однозначные чётные
    if n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n == 4:
        return 6
    elif n == 5:
        return 8

    n -= 5
    d = 2

    while True:
        min_num = 10 ** (d - 1)  # минимальное d-значное чётное
        max_num = 10**d - 2  # максимальное d-значное четное
        digits_total = ((max_num - min_num) // 2 + 1) * d  # сколько символов занимает группа

        if n <= digits_total:
            break
        n -= digits_total
        d += 1

    index_in_group = (n - 1) // d
    digit_in_number = (n - 1) % d
    number = min_num + index_in_group * 2

    # извлечь нужную цифру
    for _ in range(d - digit_in_number - 1):
        number //= 10
    return number % 10
