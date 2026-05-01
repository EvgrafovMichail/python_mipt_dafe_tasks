def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0

    i = 2
    temporary = num

    while i * i <= temporary:
        if temporary % i == 0:
            sum_of_divisors += i

            while temporary % i == 0:
                temporary /= i

        i += 1

    if temporary > 1:
        sum_of_divisors += temporary

    return sum_of_divisors
