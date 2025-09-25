def is_prime(num: int) -> int:
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**(1/2)) + 1):
            if num % i == 0:
                return False
    return True


def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0

    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            sum_of_divisors += i*is_prime(i)
            sum_of_divisors += (num//i)*is_prime(num//i)

    return sum_of_divisors
