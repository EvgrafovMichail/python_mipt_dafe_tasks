def find_single_number(nums: list[int]) -> int:
    result = 0
    for i in range(len(nums)):
        result ^= nums[i]
    return result
