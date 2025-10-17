def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0 
    divisor = 2  
    while divisor <= num:  
        simple = True
        if num % divisor == 0:

            for i in range(2, divisor):
                if divisor%i == 0:
                    simple = False
            if simple:
                sum_of_divisors += divisor  
        divisor += 1  
    return sum_of_divisors