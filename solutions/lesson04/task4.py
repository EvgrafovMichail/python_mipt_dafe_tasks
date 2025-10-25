def move_zeros_to_end(nums: list[int]) -> list[int]:
    while nums.count(0) != nums[len(nums) - nums.count(0) : len(nums)].count(0):
        nums.pop(nums.index(0))
        nums.append(0)
    return len(nums) - nums.count(0)
