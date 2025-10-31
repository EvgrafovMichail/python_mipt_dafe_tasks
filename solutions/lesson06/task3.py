def is_there_any_good_subarray(nums: list[int], k: int) -> bool:
    if len(nums) < 2:
        return False
    elif len(nums) == 2:
        sum = 0
        for subarr in nums:
            sum += subarr
        if sum % k == 0:
            return True
        else:
            return False
    for i in range(0, len(nums) - 1):
        for j in range(i + 2, len(nums) + 1):
            sum = 0
            for subarr in nums[i:j]:
                sum += subarr
            if sum % k == 0:
                return True
    return False
