def prime(n):
    if n > 1:
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                return False
        return True
    return False


def get_sum_of_prime_divisors(num):
    sum_of_divisors = 0
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            if prime(n):
                sum_of_divisors += n

                if prime(num // n) and n != num // n:
                    sum_of_divisors += num // n

    return sum_of_divisors


n = int(input())
print(get_sum_of_prime_divisors(n))
