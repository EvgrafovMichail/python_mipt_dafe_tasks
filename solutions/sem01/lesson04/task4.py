def move_zeros_to_end(nums: list[int]) -> list[int]:
    count= 0 #можно ли назвать переменную "K" и в комментарии указать, что она значит?
            #или желательно все переменные называть по их предназначению?
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count], nums[i] = nums[i], nums[count]
            count+=1
            
    
    return count

