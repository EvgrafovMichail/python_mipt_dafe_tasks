def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0 

    for i in range(2, num + 1):
        if num % i == 0:    # i - делитель числа n

            for j in range(2, i):
                if i % j ==0:   # перебираем все возможные делители числа i
                    break

            else:
                sum_of_divisors += i


    return sum_of_divisors
