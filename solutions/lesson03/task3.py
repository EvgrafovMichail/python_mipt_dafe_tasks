def get_nth_digit(num: int) -> int:
    k = 5
    i = 0
    sum_i = 0

    if num <= 5:
        digit = 0 + (num - 1) * 2
    else:
        while num > sum_i:
            i += 1
            sum_i += k
            k = (i + 1) * 45 * 10 ** (i - 1)

        sum_i = sum_i - i * 45 * 10 ** (i - 2)
        n = i

        N = 2 * ((num - sum_i) // n - 1) + 10 ** (n - 1)
        position = (num - sum_i) % n

        if position == 0:
            digit = N % 10
        else:
            digit = (N // (10 ** (n - position))) % 10

    return digit
