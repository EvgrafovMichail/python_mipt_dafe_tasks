def find_single_number(nums: list[int]) -> int:
    n = nums[0]
    for i in nums[1:]:
        n = n ^ i
    return n
