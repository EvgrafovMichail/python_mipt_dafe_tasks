def move_zeros_to_end(nums: list[int]) -> int:
    if not nums.count(0):
        return len(nums)

    n = len(nums) - nums.count(0)
    i = 0
    while i != n:
        elem = nums[i]
        if elem == 0:
            del nums[i]
            nums.append(0)
        else:
            i += 1

    return nums.index(0)
