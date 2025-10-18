def find_single_number(nums: list[int]) -> int:
    result = 0
    for i in nums:
        result ^= i
    return result
