def simple_divis(a):
    g = True
    for i in range(2, round(a**0.5) + 1):
        if a % i != 0:
            g = True
        else:
            g = False
            break
    return g


def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    if num == 1:
        return 0
    if simple_divis(num):
        sum_of_divisors += num
    for i in range(2, round(num**0.5) + 1):
        if num % i == 0:
            if simple_divis(i):
                sum_of_divisors += i
    return sum_of_divisors
