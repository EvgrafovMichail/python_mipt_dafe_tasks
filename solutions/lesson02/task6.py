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
    a = 1
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            a *= i
            if prime_or_not(i):
                sum_of_divisors += i
    for k in range(a, num + 1):
        if num % k == 0:
            if prime_or_not(num // k):
                sum_of_divisors += k
    return sum_of_divisors
