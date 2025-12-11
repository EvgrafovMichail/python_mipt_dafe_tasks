def move_zeros_to_end(nums: list[int]) -> list[int]:
    b = len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            b -= 1
        else:
            break
    i = 0
    while i < b - 1:
        while nums[i] == 0:
            for j in range(i, b - 1):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            b -= 1
        i += 1
    return b


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    print(move_zeros_to_end(a))
    print(a)
