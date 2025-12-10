def get_len_of_longest_substring(text: str) -> int:
    m=0
    for i in range(len(text)):
        for j in range(i,len(text)):
            if len(set(text[i:j+1])) == len(text[i:j+1]):
                if len(text[i:j+1])>m:
                    m=len(text[i:j+1])
    return m