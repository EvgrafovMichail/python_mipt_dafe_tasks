def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    while num > 1:
        for divisor in range(2, num + 1):
            if num % divisor == 0:
                sum_of_divisors += divisor
                while num % divisor == 0:
                    num //= divisor
                break
    return sum_of_divisors
