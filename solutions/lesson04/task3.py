def find_single_number(nums: list[int]) -> int:
    # ваш код
    answer = 0
    for num in nums:
        answer ^= num

    return answer
