def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    i = 2
    while i < num + 1:
        f = False

        while num % i == 0:
            if f == False:
                f = True
                sum_of_divisors += i
            num //= i
        i+=1
        
    return sum_of_divisors
