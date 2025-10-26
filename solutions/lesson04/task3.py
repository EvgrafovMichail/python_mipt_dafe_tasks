def find_single_number(nums: list[int]) -> int:
    ans = 0
    for elem in nums:
        ans ^= elem
    return ans
