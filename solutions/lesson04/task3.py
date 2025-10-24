def find_single_number(nums: list[int]) -> int:
    nums.sort()
    if len(nums) == 1:
        return nums[0]
    for i in range(0, len(nums) - 2, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
        else:
            return nums[-1]
