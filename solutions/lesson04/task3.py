def find_single_number(nums: list[int]) -> int:
    num = 0
    for i in nums:
        num = num ^ i
    return num
