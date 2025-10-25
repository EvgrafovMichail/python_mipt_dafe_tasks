def find_single_number(nums: list[int]) -> int:
    output = []
    j = 0
    for i in range(len(nums)):
        if nums[i] not in output:
            output.append(nums[i])
            j+=1
        else:
            output.remove(nums[i])
            j-=1
    finale = output[0]
    return finale
