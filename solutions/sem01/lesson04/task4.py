def move_zeros_to_end(nums: list[int]) -> list[int]:
    # ваш код
    insert_pos = 0
    for v in nums:
        if v != 0:
            nums[insert_pos] = v
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0

    return insert_pos
