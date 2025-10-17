def find_single_number(nums: list[int]) -> int:    
    res = 0

    for i in range(len(nums)):
        res = res ^ nums[i]
    return res
