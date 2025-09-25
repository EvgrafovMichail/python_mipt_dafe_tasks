
def get_sum_of_prime_divisors(num: int) -> int:
    if(num<=1):
        return 0
    
    if(num==2):
        return 2
    n=num
    i=1
    sum_of_divisors=0

    while(n//2+2>=i):       
        i+=1
        tf=0
        
        while(n%i==0):
            tf=1
            n//=i

        if(tf==1):
            sum_of_divisors+=i
    
    if(n>1):
        sum_of_divisors+=n
    return sum_of_divisors
