def find_single_number(nums: list[int]) -> int:
    binary_form = 0
    for num in nums:
        if num < 0:
            binary_form ^= ~(num - 1)
            binary_form *= -1
        else:
            binary_form ^= num
    return binary_form
