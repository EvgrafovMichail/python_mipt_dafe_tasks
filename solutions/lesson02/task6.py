def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    i=2
    while i-1<num:
        if num % i ==0:
            sum_of_divisors += i
            while num%i==0:
                num/=i
            i += 1 
        else:
            i+=1
    return sum_of_divisors
