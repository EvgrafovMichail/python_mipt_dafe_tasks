
def get_sum_of_prime_divisors(num: int) -> int:
    
    if num <= 1:
        return 0
    
    original_num = num
    total_sum = 0
    
    if num % 2 == 0:
        total_sum += 2
        while num % 2 == 0:
            num //= 2

    divisor = 3
    while divisor * divisor <= num:
        if num % divisor == 0:
            total_sum += divisor
            while num % divisor == 0:
                num //= divisor
        divisor += 2
    
    if num > 1:
        total_sum += num
    
    return total_sum