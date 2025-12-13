def move_zeros_to_end(nums: list[int]) -> int:
    ne_nol = 0
    for digit in nums:
        if digit != 0:
            ne_nol += 1
    if ne_nol == len(nums):
        return len(nums)
    if ne_nol == 0:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return ne_nol
