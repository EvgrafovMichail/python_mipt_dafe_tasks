def get_sum_of_prime_divisors(num: int) -> int:
    result = 0
    if num >= 2:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                result += i
                while num % i == 0:
                    num //= i
            if num == 1:
                break
        if result == 0:
            return num
    return result
