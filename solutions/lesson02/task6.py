def get_sum_of_prime_divisors(num: int) -> int:
    if num==1:
        return 0
    sum_of_divisors = PrimeDivisors(num)
    return sum_of_divisors

def IsPrime(n):
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True

def PrimeDivisors(n):
    divisors = []
    if IsPrime(n):
        divisors.append(n)
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            if IsPrime(i):
                divisors.append(i)
            if IsPrime(n//i):
                divisors.append(n//i)
    return sum(divisors)