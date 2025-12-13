def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    ostats = {i: nums[i] % k for i in range(len(nums))}

    for x in range(len(nums)):
        sum_ost = 0
        kol = 0

        for y in range((x), len(nums)):
            sum_ost += ostats[y]
            kol += 1

            if sum_ost % k == 0 and kol >= 2:
                return True

    return False
