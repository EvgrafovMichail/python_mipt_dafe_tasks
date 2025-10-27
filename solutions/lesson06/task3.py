def is_there_any_good_subarray(nums: list[int], k: int) -> bool:
    amount_by_mod_k = {0: -1}
    summa = 0
    for index in range(len(nums)):
        summa = (summa + nums[index]) % k
        if summa in amount_by_mod_k:
            if index - amount_by_mod_k[summa] >= 2:
                return True
        else:
            amount_by_mod_k[summa % k] = index
    return False


print(is_there_any_good_subarray([5, 2], 3))
