def proverka_na_prostoe(i: int) -> int:
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return 0

    return i


def get_sum_of_prime_divisors(num: int) -> int:
    if num == 1:
        return 0

    elif proverka_na_prostoe(num) != 0:
        return num

    else:
        sum_of_divisors = 0

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # i - делитель числа n, num/i - тоже
                sum_of_divisors += proverka_na_prostoe(i) + proverka_na_prostoe(num // i)

    return sum_of_divisors
