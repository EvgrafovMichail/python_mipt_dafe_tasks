def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    if is_prime(num) and num != 1:
        return num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                sum_of_divisors += i
            if is_prime(num // i):
                sum_of_divisors += num // i
    return sum_of_divisors
