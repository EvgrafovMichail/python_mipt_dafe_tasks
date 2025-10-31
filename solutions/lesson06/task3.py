def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    dict = {}
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        c = s % k
        if c == 0 and i > 0:
            return True
        if c in dict.keys():
            if i - dict[c] >= 2:
                return True
            dict[c] = min(dict[c], i)
        else:
            dict[c] = i
    # ваш код
    return False
