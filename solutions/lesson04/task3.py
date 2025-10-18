def find_single_number(nums: list[int]) -> int:
    binary_form = 0
    for num in nums:
        binary_form ^= num
    return binary_form
