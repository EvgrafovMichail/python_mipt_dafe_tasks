def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    # ваш код
    if num <= 1:
        return 0  
    prime_divisors = set()
    temp = num
    if temp % 2 == 0:
        prime_divisors.add(2)
        while temp % 2 == 0:
            temp //= 2
    divisor = 3
    while divisor * divisor <= temp:
        if temp % divisor == 0:
            prime_divisors.add(divisor)  # divisor будет простым, так как мы идем от меньшего к большему
            while temp % divisor == 0:
                temp //= divisor
        divisor += 2

    if temp > 1:
        prime_divisors.add(temp)
    
    sum_of_divisors =sum(prime_divisors)
    return sum_of_divisors
