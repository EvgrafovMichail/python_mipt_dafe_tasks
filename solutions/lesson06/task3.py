def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if sum(nums[i : j + 1]) % k == 0:
                return True
    return False
