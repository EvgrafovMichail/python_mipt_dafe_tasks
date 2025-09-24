
def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors=0
    for i in range(num,1,-1):
        tf=0
        if(num%i==0):
            for i2 in range(2,int(i**0.5)+1):
                if(i%i2==0):
                    tf=1
                    break

            if tf==0:
                sum_of_divisors=sum_of_divisors+i

    return sum_of_divisors
