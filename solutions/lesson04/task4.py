def move_zeros_to_end(nums: list[int]) -> int:
    zero_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_pos], nums[i] = nums[i], nums[zero_pos]
            zero_pos += 1

    return zero_pos
