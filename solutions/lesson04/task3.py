def find_single_number(nums: list[int]) -> int:
    c = 0
    for i in nums:
        c = c ^ i
    return c
