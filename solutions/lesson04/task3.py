def find_single_number(nums: list[int]) -> int:
    x = 0
    for i in nums:
        x  ^= i
    return x


nums = [1, 1, 1, 2]
print(find_single_number(nums))