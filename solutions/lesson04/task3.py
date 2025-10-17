def find_single_number(nums: list[int]) -> int:
    
    result = 0
    for candidate in nums:
        result ^= candidate
    
    return result