def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    have = {}
    summ = 0
    for i in range(len(nums)):
        summ += nums[i]
        summ %= k
        if summ in have and i - have[summ] >= 2 or summ == 0 and i > 0:
            return True
        if summ not in have:
            have[summ] = i
    return False
