def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    if len(nums) < 2:
        return False

    if (nums[0] + nums[1]) % k == 0:
        return True
    elif len(nums) == 2:
        return False
    last = (nums[1] + nums[0]) % k
    der = {nums[0] % k}

    for i in range(2, len(nums)):
        curr = (nums[i] + last) % k

        if curr in der:
            return True

        der.add(last)
        last = curr

    return False
