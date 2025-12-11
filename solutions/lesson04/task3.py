def find_single_number(nums: list[int]) -> int:
    mask = 0
    for number in nums:
        mask ^= number

    return mask
