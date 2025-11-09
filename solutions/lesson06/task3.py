def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    n = len(nums)
    for i1 in range(n - 1):
        sum = nums[i1]
        for i2 in range(i1 + 1, n):
            sum += nums[i2]
            if sum % k == 0:
                return True

    return False
