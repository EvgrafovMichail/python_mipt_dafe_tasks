def move_zeros_to_end(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] == 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            return i + 1
    return 0
