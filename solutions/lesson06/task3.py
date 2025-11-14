def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    mods = {0: -1}
    sum_nums = 0
    for i in range(len(nums)):
        sum_nums += nums[i]
        nums_mod = sum_nums % k
        if nums_mod in mods:
            if i - mods[nums_mod] >= 2:
                return True
        else:
            mods[nums_mod] = i

    return False


# print(is_there_any_good_subarray([23, 2, 6, 4, 7], 13))
