def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    for l in range(len(nums) - 1):
        for r in range(l+1, len(nums)):
            if sum(nums[l:r + 1]) % k == 0:
                return True
    return False
