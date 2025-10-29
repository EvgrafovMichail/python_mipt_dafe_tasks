def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
     for i in range(len(nums)-1):
        good_arr = []
        good_arr.append(nums[i])
        for j in range(i+1, len(nums)):
            good_arr.append(nums[j])
            if  sum(good_arr) ==0 or sum(good_arr)%k == 0 :
                return True
    return False
