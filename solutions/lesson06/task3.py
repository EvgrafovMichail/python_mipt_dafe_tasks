def is_there_any_good_subarray(nums: list[int], k: int) -> bool:
    # ваш код
    for i in range(len(nums)):
        sum = nums[i]
        for g in range(i + 1, len(nums)):
            sum += nums[g]
            if sum % k == 0:
                return True
    return False
