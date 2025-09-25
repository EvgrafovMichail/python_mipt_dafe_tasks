def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    prime = True

    if num == 1:
        get_sum_of_prime_divisors = 0
    else:
        for i in range(2, num + 1):
            prime = True
            if num % i == 0:
                for j in range(2, i):
                    if i % j == 0:
                        prime = False
                        break
                if prime:
                    sum_of_divisors += i
    return sum_of_divisors
