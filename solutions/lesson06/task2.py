def get_len_of_longest_substring(text: str) -> int:
    char_index = {}  
    left_ind = 0
    max_len = 0
    
    for right_ind in range(len(text)):
        char = text[right_ind]
        if char in char_index and char_index[char] >= left_ind:
            left_ind = char_index[char] + 1  
        
        char_index[char] = right_ind
        
        max_len = max(max_len, right_ind - left_ind + 1)
    
    return max_len
