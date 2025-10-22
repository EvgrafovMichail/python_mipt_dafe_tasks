def get_nth_digit(num: int) -> int:
    # ваш код

    n_digit = 1

    while True:
        if n_digit == 1:
            number_of_digits = 5
        else:
            number_of_digits = n_digit * (9 * 10 ** (n_digit - 1)) // 2
        if num <= number_of_digits:
            break

        num -= number_of_digits
        n_digit += 1

    if n_digit == 1:
        index = (num - 1) // n_digit
        figure = 2 * index
        position = (num - 1) % n_digit
    else:
        index = (num - 1) // n_digit
        first_figure = 10 ** (n_digit - 1)
        figure = first_figure + 2 * index
        position = (num - 1) % n_digit

    while (position + 1) != n_digit:
        figure //= 10
        position += 1

    return figure % 10
