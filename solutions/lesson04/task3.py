def find_single_number(nums: list[int]) -> int:
    n = 0
    for i in nums:
        n ^= i
    return n
