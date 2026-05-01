def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    arr_ost = [0]
    next_sum = 0 
      
    for i in range(len(nums)):  
        next_sum += nums[i]
        ost = next_sum % k

        if ost in arr_ost:
            print(arr_ost.index(ost), i, arr_ost)
            if i - arr_ost.index(ost) >= 2:
                return True
            else:
               arr_ost.append(ost) 
        
        else:
            arr_ost.append(ost)
    
    if (len(arr_ost) - 1) - arr_ost.index(arr_ost[-1]) >= 2:
        return True
    
    return False

