def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    # ваш код
    
    numbers = set()

    def searching_for_a_divisor(num):
        for i in range (2, num + 1):
            if num % i == 0:
                return i

    if num == 1:
        return 0
    else:
        while (num != 1):
            divisor = searching_for_a_divisor(num)
            numbers.add(divisor)
            num //= divisor

    sum_of_divisors = sum(numbers)
    return sum_of_divisors
