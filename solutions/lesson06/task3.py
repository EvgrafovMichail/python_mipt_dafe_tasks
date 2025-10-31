def is_there_any_good_subarray(nums: list[int], k: int) -> bool:
    s = 0
    d = {0: -1}
    for i in range(len(nums)):
        s = (s + nums[i]) % k
        if s in d:
            if i - d[s] >= 2:
                return True
        else:
            d[s] = i
    return False
