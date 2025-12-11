def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    # ваш код

    divisor = 0

    if num == 1:
        return 0
    else:
        while num != 1:
            for i in range(2, num + 1):
                if num % i == 0:
                    prev_divisor = divisor
                    divisor = i
                    break
            num //= divisor
            if prev_divisor != divisor:
                sum_of_divisors += divisor

    return sum_of_divisors
