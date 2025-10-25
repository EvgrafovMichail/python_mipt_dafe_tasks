def move_zeros_to_end(nums: list[int]) -> list[int]:
    index = 0
    i = 0
    j = 0
    N = len(nums)
    while i < N:
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
        i += 1

    index = j
    while j < N:
        nums[j] = 0
        j += 1
    return index
