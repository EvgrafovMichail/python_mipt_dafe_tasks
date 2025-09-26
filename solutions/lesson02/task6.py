def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and num_is_simple(i):
            sum_of_divisors += i
    if sum_of_divisors == 0 and num != 1:
        sum_of_divisors += num
    return sum_of_divisors


def num_is_simple(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
