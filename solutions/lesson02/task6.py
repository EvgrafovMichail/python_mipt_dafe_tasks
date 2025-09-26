def get_sum_of_prime_divisors(num: int) -> int:
    sum_of_divisors = 0
    if num == 1:
        return 0
    for i in range(int(num**0.5) + 1, 1, -1):
        if num % i == 0:
            for k in range(2, int(i**0.5) + 2):
                if k == int(i**0.5) + 1:
                    sum_of_divisors += i
                elif i % k == 0:
                    break
                else:
                    continue
    if sum_of_divisors == 0:
        sum_of_divisors = num

    return sum_of_divisors
