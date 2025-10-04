def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    if is_prime(num) and num != 1:
        return num
    cnt = 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            cnt += 1
            if is_prime(i):
                sum_of_divisors += i
            # if is_prime(num // i):
            #     sum_of_divisors += num // i
    if cnt == 1:
        sum_of_divisors += num // sum_of_divisors 
    return sum_of_divisors
