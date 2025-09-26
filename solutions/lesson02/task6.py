def get_sum_of_prime_divisors(num: int) -> int:
    su = 0
    if num > 100:
        j = int(num**0.5)
    else:
        j = num

    if num >= 2:
        for i in range(2, j + 1):
            if num % i == 0:
                su += i
                while num % i == 0:
                    num //= i
    return su
