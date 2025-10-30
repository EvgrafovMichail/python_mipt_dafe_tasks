def is_there_any_good_subarray(
    s: list[int],
    n: int,
) -> bool:
    
    my_dict = {}
    sum = 0
    if len(s) == 2: 
        return (s[0] + s[1]) % n == 0
    
    for i in range(len(s)):
        sum += s[i]
        if (sum % n) not in my_dict:
            my_dict[sum % n] = i
        else:
            if i - my_dict[sum % n] >= 2:
                return True
    return False
