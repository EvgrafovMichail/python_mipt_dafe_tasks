def IsPrime(num: int) -> bool:
    d = 2
    while num % d != 0:
        d += 1
    return d == num


def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    divisors = []
    i = 2
    while num != 1:
        if num % i == 0:
            if IsPrime(i):
                divisors.append(i)
                num //= i
                i = 2

        else:
            i += 1
    divisors = set(divisors)
    for i in divisors:
        sum_of_divisors += i
    return sum_of_divisors
