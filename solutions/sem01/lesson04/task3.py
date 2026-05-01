def find_single_number(nums: list[int]) -> int:
    m = nums[0]

    for i in nums[1:]:
        m = m ^ i

    return m
