def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    div = 2
    while div * div <= num:
        if num % div == 0:
            sum_of_divisors += div
            while num % div == 0:
                num //= div
        div += 1
    if num > 1:
        sum_of_divisors += num

    return sum_of_divisors
