def move_zeros_to_end(nums: list[int]) -> list[int]:
    j = 0
    ln_nums = len(nums)
    hod = 0
    while hod != ln_nums:
        if nums[j] == 0:
            nums.insert(ln_nums, nums.pop(j))
            hod += 1
        else:
            hod += 1
            j += 1
    return j
