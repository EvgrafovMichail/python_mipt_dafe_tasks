def find_single_number(nums: list[int]) -> int:
    unique = 0
    for i in nums:
        unique ^= i
    return unique


# print(find_single_number([2, 2, 3, 3, 4]))
