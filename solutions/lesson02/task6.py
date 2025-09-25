def prost(num):
    if num == 1:
        return False 
    for divisor in range(2, int(num**0.5) + 1): 
        if num % divisor == 0: 
            return False 
    return True

def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    # ваш код
    if prost(num):
        sum_of_divisors = num
    else:
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                if prost(divisor):
                    sum_of_divisors += divisor
                if prost(num // divisor):
                    sum_of_divisors += (num // divisor)
    return sum_of_divisors