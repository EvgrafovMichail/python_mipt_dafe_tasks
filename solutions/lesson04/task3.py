def find_single_number(nums: list[int]) -> int:
    for i in nums:
        if nums.count(i) == 1:
            return i
    return 0
