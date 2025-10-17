def find_single_number(nums: list[int]) -> int:
    value = 0
    for num in nums:
        value ^= num
    return value
