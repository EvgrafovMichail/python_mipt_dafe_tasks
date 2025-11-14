def move_zeros_to_end(nums: list[int]) -> list[int]:
    i = 0
    j = 0

    while i < (len(nums)):
        if nums[j] == 0:
            nums.append(nums[j])
            del nums[j]
            i += 1

        else:
            i += 1
            j += 1

    if (0) not in nums:
        return len(nums)

    return len(nums) - nums.count(0)
