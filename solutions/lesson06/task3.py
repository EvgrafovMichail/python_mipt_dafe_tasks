def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    seen = {}
    total_sum = 0
    seen[0] = -1

    for i in range(len(nums)):
        total_sum += nums[i]
        remainder = total_sum % k

        if remainder in seen:
            if i - seen[remainder] > 1:
                return True
        else:
            seen[remainder] = i

    return False
