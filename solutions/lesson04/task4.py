def move_zeros_to_end(nums: list[int]) -> list[int]:
    flag = False
    for i in range(len(nums)):
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
            flag = True
    if flag == True:
        return nums.index(0)
    else:
        return len(nums)

#print(move_zeros_to_end([1, 0, 0]))