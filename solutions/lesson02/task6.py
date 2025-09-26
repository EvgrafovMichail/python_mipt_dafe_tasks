def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    deliteli = []
    for i in range(2, num + 1):
        if num % i == 0:
            deliteli.append(i)
    for i in range(len(deliteli)):
        for j in range(2, deliteli[i]):
            if deliteli[i] % j == 0:
                deliteli.pop(i)
    for i in range(len(deliteli)):
        sum_of_divisors += deliteli[i]

    return sum_of_divisors
