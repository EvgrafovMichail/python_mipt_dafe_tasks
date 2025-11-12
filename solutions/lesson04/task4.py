def move_zeros_to_end(nums: list[int]) -> list[int]:
    value = nums.count(0)
    mask = [x for x in nums if x != 0]
    for i in range(0, len(nums)):
        if i < len(mask):
            nums[i] = mask[i]
        else:
            nums[i] = 0
    return len(nums) - value
