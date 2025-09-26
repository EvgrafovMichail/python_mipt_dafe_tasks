def is_prime(num):
    if num == 2 or num == 3: 
        return True
    if num <= 1 or num % 2 == 0: 
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0: 
            return False
    return True

def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    if num >= 2:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0 and is_prime(i):
                sum_of_divisors += i
    if is_prime(num): 
        sum_of_divisors += num
    return sum_of_divisors