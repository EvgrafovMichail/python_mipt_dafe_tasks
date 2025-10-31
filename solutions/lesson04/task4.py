def move_zeros_to_end(nums: list[int]) -> list[int]:
    i = 0
    j = 0  # счетчик нулей
    if len(nums) == 1 and nums[0] == 0:
        return nums, 0
    while i < len(nums):
        if nums[i] == 0:
            nums.append(0)
            nums.pop(i)
            j += 1
        else:
            i += 1
    long = len(nums) - j
    return nums, long
