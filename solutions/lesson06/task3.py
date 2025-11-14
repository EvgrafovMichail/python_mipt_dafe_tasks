def is_there_any_good_subarray(nums: list[int], k: int) -> bool:
    if (nums == "") or (k == 0):
        return False

    for start_ind in range(len(nums)):
        sum = 0

        for i in range(start_ind, len(nums)):
            sum += nums[i]
            if (i != start_ind) and (sum % k == 0):
                return True

    return False
