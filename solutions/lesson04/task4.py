def move_zeros_to_end(nums: list[int]) -> list[int]:
    if not nums:    
        return 0
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0
    return index if index < len(nums) else len(nums)