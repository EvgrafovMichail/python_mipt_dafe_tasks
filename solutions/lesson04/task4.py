def move_zeros_to_end(nums: list[int]) -> list[int]:
    # ваш код
    counter = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[counter], nums[i] = nums[i], nums[counter]
            counter += 1

    return counter
