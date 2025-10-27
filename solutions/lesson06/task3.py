def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    for i in range(2, len(nums) + 1):
        for j in range(len(nums) - i + 1):
            summar = nums[j]
            for elem in range(1, i):
                summar += nums[j + elem]
            if is_multiples(summar, k):
                return True
    return False


def is_multiples(num1: int, num2: int) -> bool:
    if num1 == 0 or num2 == 0:
        return True
    return num1 % num2 == 0
