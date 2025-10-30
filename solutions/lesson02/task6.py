def get_sum_of_prime_divisors(num: int) -> int:
    # ваш код
    if num < 2:
        return 0
    s, f = 0, 2
    while f * f <= num:
        if num % f == 0:
            s += f
            while num % f == 0:
                num //= f
        f += 1
    if num > 1:
        s += num
    return s
