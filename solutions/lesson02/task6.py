def get_sum_of_prime_divisors(num: int) -> int:
    nums = set()
    while num != 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                num //= i
                nums.add(i)
                break
        else:
            nums.add(num)
            break
    return sum(nums)
