def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    sqrt_num = 1

    while sqrt_num * sqrt_num < num:
        sqrt_num += 1
    sqrt_num -= sqrt_num * sqrt_num > num

    for divisor in range(2, sqrt_num + 1):
        if num % divisor == 0:
            is_prime = 1
            sqrt_div = 1
            while sqrt_div * sqrt_div < divisor:
                sqrt_div += 1
            sqrt_div -= sqrt_div * sqrt_div > divisor
            for to_check in range(2, sqrt_div + 1):
                if divisor % to_check == 0:
                    is_prime = 0
                    break
            if is_prime:
                sum_of_divisors += divisor

            is_prime = 1
            extra_divisor = num // divisor
            sqrt_extra = 1
            while sqrt_extra * sqrt_extra < extra_divisor:
                sqrt_extra += 1
            sqrt_extra -= sqrt_extra * sqrt_extra > extra_divisor
            for to_check in range(2, sqrt_extra + 1):
                if extra_divisor % to_check == 0:
                    is_prime = 0
                    break
            if is_prime and extra_divisor != divisor:
                sum_of_divisors += extra_divisor

    if sum_of_divisors == 0 and num != 1:
        return num

    return sum_of_divisors
