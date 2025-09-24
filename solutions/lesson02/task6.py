def prime(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    for t in range(2, int(x ** 0.5) + 1):
        if x % t == 0:
            return 0
    return 1
def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and prime(i):
            sum_of_divisors += i
        if num % (num//i) == 0 and prime(num//i):
            sum_of_divisors += (num//i)
    if prime(num):
        sum_of_divisors += num
    return sum_of_divisors
print(get_sum_of_prime_divisors(1))