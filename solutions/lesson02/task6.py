def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                sum_of_divisors += i
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        sum_of_divisors += num
    return sum_of_divisors * (num != 1)