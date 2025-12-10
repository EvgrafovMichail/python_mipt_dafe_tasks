def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0

    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                sum_of_divisors += i
                while num % i == 0:
                    num //= i

                break

    return sum_of_divisors
