def get_len_of_longest_substring(a: str) -> int:
    a_dict = {}  
    max_len = 0
    left = 0  
    
    for right in range(len(a)):
        
        if a[right] in a_dict and a_dict[a[right]] >= left:
            left = a_dict[a[right]] + 1
        max_len = max(max_len, right - left + 1)
        a_dict[a[right]] = right
       
    
    return max_len


