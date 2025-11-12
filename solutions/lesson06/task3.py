def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    for i in range(len(nums)):
        if i + 2 < len(nums):
            for j in range(i + 2, len(nums)):
                if sum(nums[i:j]) % k == 0:
                    return True
    if len(nums) >= 2:
        if (nums[-1] + nums[-2]) % k == 0:
            return True
    return False
