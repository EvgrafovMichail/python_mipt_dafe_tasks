def move_zeros_to_end(nums: list[int]) -> list[int]:
    n = 0
    for i in range(l := len(nums)):
        if nums[i] != 0:
            nums[n] = nums[i]
            n += 1
    for i in range(n, l):
        nums[i] = 0
    return n