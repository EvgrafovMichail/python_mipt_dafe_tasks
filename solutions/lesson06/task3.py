def is_there_any_good_subarray(nums: list[int], k: int) -> bool:
    nums_len = len(nums)
    for i in range(nums_len - 1):
        s = nums[i]
        for j in range(i + 1, nums_len):
            s += nums[j]
            if s % k == 0:
                return True

    return False
