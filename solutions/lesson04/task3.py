def find_single_number(nums: list[int]) -> int:
    s = [0] * (2 * 10**6)
    for num in nums:
        s[num + 10**6] += 1
    return s.index(1) - 10**6
