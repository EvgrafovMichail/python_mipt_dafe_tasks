def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    for lenpods in range(1, len(nums) + 1):
        for i in range(len(nums) - lenpods):
            if sum(nums[i : i + lenpods + 1]) % k == 0:
                return True
    return False
