def get_len_of_longest_substring(text: str) -> int:
    res = ""
    maxi = 0
    for i in range(len(text)):
        if text[i] not in res:    
            res += text[i]
        else:
            maxi = max(maxi, len(res))
            res = res[res.find(text[i])+1:] + text[i]
    maxi = max(maxi, len(res))
    return maxi
