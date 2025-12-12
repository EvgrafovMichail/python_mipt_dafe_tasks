def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    remains = dict()
    sum_pred = 0
    j = 0
    for i in nums:
        sum_pred += i
        rem = sum_pred % k
        if rem == 0 and j >= 1:
            return True
        if rem in remains:
            if j - remains[rem] >= 2:
                return True
        else:
            remains[rem] = j
        j += 1
    return False


print(is_there_any_good_subarray([23, 2, 6, 4, 7], 13))
