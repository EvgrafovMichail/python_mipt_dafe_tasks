def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    for left in range(len(nums)):
        current_sum = nums[left]
        for r in range(left + 1, len(nums)):
            current_sum += nums[r]
            if current_sum % k == 0:
                return True
    return False
