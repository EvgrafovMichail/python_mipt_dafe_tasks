def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    for left in range(len(nums) - 1):
        sumK = nums[left]
        for r in range(left + 1, len(nums)):
            sumK += nums[r]
            if sumK % k == 0:
                return True
    return False
