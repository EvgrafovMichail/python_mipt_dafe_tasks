def get_sum_of_prime_divisors(num: int) -> int:

    nums={0}

    def divider(num):
        for i in range(2,num+1):
            if num % i == 0:
                return i
        return False
    if num==1: return 0
    else:
        while num != 1:
            x = divider(num)
            if x: 
                nums.add(x)
                num //= x

        return sum(nums)