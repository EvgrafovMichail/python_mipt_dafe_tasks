num = int(input())#по факту самое важное, что если число составное, то будет множитель до корня из нам(я это вот только что узнал) и то, что 2 покрывае все четные числа(ну это очев)
def get_sum_of_prime_divisors(num: int) -> int:

    sum_of_divisors = 0
    if num%2 ==0:
        sum_of_divisors+=2 
    x =3
    while x**2 <=num:
        if num%x == 0:
            sum_of_divisors += x
            while num%x == 0:
                num/=x
        x = x+2
    return sum_of_divisors
print(get_sum_of_prime_divisors(num))