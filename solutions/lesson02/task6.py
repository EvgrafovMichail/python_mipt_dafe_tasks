
def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    t=int(num**0.5)
    d=0
    if(num == 1):
        return 0
    else:
        for i in range (1, t+1):
            if (num%i != 0):
                continue
            if (num%i == 0) :
                d=0
                for j in range (1, int(i**0.5)+1):
                    if (i%j == 0 and j != 1):
                        d += 1    
                if (d == 0):
                    sum_of_divisors += i
                d=0
                for k in range (1, int((num/i)**(0.5))+1) :
                    if (int(num/i)%k==0 and k !=1 ):
                        d += 1
                if (d == 0):
                    sum_of_divisors += int(num/i)
        return sum_of_divisors-1
 
