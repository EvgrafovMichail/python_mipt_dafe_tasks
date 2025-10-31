def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    s = 0
    rems = {0: -1}
    for i in range(len(nums)):
        s += nums[i]
        if s % k in rems:
            if i - rems[s % k] >= 2:
                return True
        else:
            rems[s % k] = i
    return False
