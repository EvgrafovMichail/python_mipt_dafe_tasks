def find_single_number(nums: list[int]) -> int:
    # ваш код
    nums = sorted(nums)
    unique = 0
    for num in nums:
        unique ^= num
    return unique
