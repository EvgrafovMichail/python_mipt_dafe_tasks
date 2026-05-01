def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    d = {}
    sum = 0

    for i in range(len(nums)):
        sum += nums[i]
        r = sum % k

        if r == 0 and i >= 1:
            return True

        if r in d:
            if i - d[r] > 1:
                return True
        else:
            d[r] = i

    return False
