def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if j - i >= 1 and curr_sum % k == 0:
                return True
    return False
