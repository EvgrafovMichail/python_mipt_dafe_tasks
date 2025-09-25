def prime(n):
    if n > 1: 
        for d in range(2, int(n ** 0.5) + 1): 
            if n % d == 0: 
                return False
        return True
    return False

    


def get_sum_of_prime_divisors(num):
    sum_of_divisors = 0
    for n in range(1, int(num ** 0.5) + 1):
        if num % n == 0 and prime(n):
            sum_of_divisors += n
        elif num % n == 0 and prime(num // n):
            sum_of_divisors += num // n

    return sum_of_divisors
