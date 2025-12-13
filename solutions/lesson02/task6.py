def get_sum_of_prime_divisors(num: int) -> int:
    su = 0
    if num >= 2:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                su += i
                while num % i == 0:
                    num //= i
            if num == 1:
                break
        if su == 0:
            return num
    return su
