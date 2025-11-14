def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum_of_divisors += i
        while num % i == 0:
            num //= i
        i += 1
    if num > 1:
        sum_of_divisors += num
    return sum_of_divisors
