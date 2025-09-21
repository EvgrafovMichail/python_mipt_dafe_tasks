def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    i=2
    a=num
    
    while i<=num//2 and a!=1:
        
        if num%i==0:
            sum_of_divisors+=i
            while a%i==0:
                a//=i
        
        i+=1
    
    if a==num:
        sum_of_divisors = num

    return sum_of_divisors
