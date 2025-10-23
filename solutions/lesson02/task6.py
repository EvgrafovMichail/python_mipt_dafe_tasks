def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    mult_of_divisors = 1
    while num != 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                num //= i
                if mult_of_divisors % i != 0:
                    sum_of_divisors += i
                    mult_of_divisors *= i
                break
        else:
            if mult_of_divisors % num != 0:
                sum_of_divisors += num
            break

    return sum_of_divisors
