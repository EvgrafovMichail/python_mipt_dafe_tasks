def move_zeros_to_end(nums: list[int]) -> list[int]:
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1

    return pos
