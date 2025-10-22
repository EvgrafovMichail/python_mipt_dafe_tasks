def move_zeros_to_end(nums: list[int]) -> list[int]:
    # ваш код
    not_0 = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[not_0] = nums[i]
            not_0 += 1
    for i in range(not_0, len(nums)):
        nums[i] = 0

    return not_0
