def prime_or_not(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    if prime_or_not(num):
        return num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if prime_or_not(i):
                sum_of_divisors += i
            if prime_or_not(num // i) and num % (num // i) == 0:
                sum_of_divisors += num // i
    return sum_of_divisors
