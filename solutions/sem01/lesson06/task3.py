def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    current = {0: -1}
    summa = 0
    for i in range(len(nums)):
        summa += nums[i]
        ost = summa % k
        if ost in current:
            if i - current[ost] >= 2:
                return True
        else:
            current[ost] = i
    return False
