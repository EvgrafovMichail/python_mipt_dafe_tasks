def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    n = 2
    while n - 1 < num:
        if num % n == 0:
            sum_of_divisors += n
            while num % n == 0:
                num /= n
            n += 1
        else:
            n += 1
    return sum_of_divisors
