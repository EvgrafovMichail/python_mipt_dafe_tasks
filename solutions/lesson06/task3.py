def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    if len(nums) < 2:
        return False
    if k == 1:
        return True
    dic = {0: -1}
    c = 0
    for i in range(len(nums)):
        c += nums[i] % k
        if c % k not in dic:
            dic[c % k] = i

        else:
            if i - dic[c % k] >= 2:
                return True
            else:
                continue

    return False
