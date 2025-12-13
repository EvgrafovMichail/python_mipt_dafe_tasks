def move_zeros_to_end(nums: list[int]) -> list[int]:
    a = len(nums)
    x = 0
    for i in range(0, a):
        if nums[i] == 0:
            x += 1
    y = a - x
    z = 0
    for i in range(0, a):
        if nums[i] != 0:
            nums[z] = nums[i]
            z += 1
    for i in range(y, a):
        if nums[i] != 0:
            nums[i] = 0
    return y
