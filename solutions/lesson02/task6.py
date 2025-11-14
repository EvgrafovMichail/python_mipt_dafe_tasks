def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    if num % 2 == 0:
        sum_of_divisors += 2
        while num % 2 == 0:
            num //= 2
    x = 3
    while x**2 <= num:
        if num % x == 0:
            sum_of_divisors += x
            while num % x == 0:
                num //= x
        x = x + 2
    if num > 1:
        sum_of_divisors += num
    return sum_of_divisors
