def prost(num):
    if num == 1:
        return False
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False
    return num


def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    # ваш код
    if prost(num):
        sum_of_divisors = num
    else:
        for divisor in range(2, num + 1):
            if num % divisor == 0:
                if prost(divisor):
                    sum_of_divisors += divisor
    return sum_of_divisors


def get_sum_of_prime_divisors2(num: int) -> int:
    sum_of_divisors = 0
    # ваш код
    if prost(num):
        sum_of_divisors = num
    else:
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                sum_of_divisors += prost(divisor) + prost(num // divisor)
    return sum_of_divisors


print(get_sum_of_prime_divisors2(9))
