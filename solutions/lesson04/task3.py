def find_single_number(nums: list[int]) -> int:
    res = 0
    for n in nums:
        res ^=n
    return res

