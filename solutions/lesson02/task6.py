def get_sum_of_prime_divisors(num: int) -> int:
    n = num
    if n == 1:
        return 0
    sum_of_divisors = 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            while num % i == 0:
                num //= i
    if sum_of_divisors == 0:
        return n
    return sum_of_divisors
