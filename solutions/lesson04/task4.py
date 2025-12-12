def move_zeros_to_end(nums: list[int]) -> list[int]:
    slot0 = 0
    for i in nums:
        if i != 0:
            nums[slot0] = i
            slot0 += 1
        else:
            pass
    for i in range(slot0, len(nums)):
        nums[i] = 0

    return slot0
