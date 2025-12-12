def find_single_number(nums: list[int]) -> int:
    res = 0
    for i in nums:
        res ^= i
    return res
