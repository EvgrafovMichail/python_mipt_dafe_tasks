def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0

    if num == 1:
        return 0

    for delit in range(2, num + 1):
        if num % delit == 0:
            sum_of_divisors += delit
            while num % delit == 0:
                num //= delit

    if sum_of_divisors == 0:
        return num

    return sum_of_divisors


# print(get_sum_of_prime_divisors(int(input("num = "))))
