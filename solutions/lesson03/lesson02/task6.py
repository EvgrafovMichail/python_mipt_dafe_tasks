def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    k = 0
    if num <= 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            k = 1
            break
    if k == 0:
        sum_of_divisors = num
    for i in range(2, int(num**0.5) + 1):
        c = 0
        if num % i == 0:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    c = 1
                    break
            if c == 0:
                sum_of_divisors += i

    return sum_of_divisors
