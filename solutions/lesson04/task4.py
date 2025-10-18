def move_zeros_to_end(nums: list[int]) -> list[int]:
    position = 0

    for num in range(len(nums)):
        if nums[num] != 0:
            nums[position] = nums[num]
            position += 1

    for num_2 in range(position, len(nums)):
        nums[num_2] = 0

    return position
