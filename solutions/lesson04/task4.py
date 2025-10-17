def move_zeros_to_end(nums: list[int]) -> list[int]:
    sch = len(nums) - 1
    i = -1
    while sch >= 0:
        i += 1
        if nums[i] == 0:
            for j in range(i, len(nums) - 1):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            i -= 1

        sch -= 1
    c = nums.count(0)
    return len(nums) - c
