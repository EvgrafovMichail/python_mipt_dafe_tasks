def find_single_number(nums: list[int]) -> int:
    c = 0
    for x in nums:
        c ^= x
    return c
