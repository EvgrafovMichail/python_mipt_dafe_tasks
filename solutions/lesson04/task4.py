def move_zeros_to_end(nums: list[int]) -> list[int]:
    zero_offset = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zero_offset -= 1
        else:
            nums[i + zero_offset] = nums[i]

    for i in range(zero_offset, 0):
        nums[i] = 0

    return len(nums) + zero_offset
