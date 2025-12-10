def find_single_number(nums: list[int]) -> int:
    nums = sorted(nums)

    if len(nums) == 1:
        return nums[0]

    if nums[len(nums) - 1] != nums[len(nums) - 2]:
        return nums[len(nums) - 1]

    for i in range(0, len(nums), 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
