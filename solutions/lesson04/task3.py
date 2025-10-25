def find_single_number(nums: list[int]) -> int:
    imposter = 0
    for i in range(len(nums)):
        if nums.count(nums[i]) != 2:
            imposter = nums[i]
    return imposter
