def move_zeros_to_end(nums: list[int]) -> list[int]:
    zeros = 0
    for x in nums:
        if x == 0:
            zeros += 1
    for i in range(zeros):
        nums.remove(0)
    nums += [0]*zeros
    return len(nums) - zeros