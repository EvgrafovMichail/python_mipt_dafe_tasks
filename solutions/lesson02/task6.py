def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    denumerator = 2
    original = num
    while num != 1 and denumerator ** 2 <= original:
        if num % denumerator == 0:
            sum_of_divisors += denumerator
            while num % denumerator == 0:
                num //= denumerator
        denumerator += 1
    if num != 1:
        sum_of_divisors += num
    return sum_of_divisors
