def find_single_number(nums: list[int]) -> int:
    answer = 0

    for number in nums:
        answer ^= number

    return answer
