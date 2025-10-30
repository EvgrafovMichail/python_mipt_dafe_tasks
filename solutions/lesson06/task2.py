def get_len_of_longest_substring(text: str) -> int:
    l = 0
    n = len(text)
    for i in range(len(text)):
        for j in range (i+1, n+1):
            s = text[i : j]
            if len(s) == len(set(s)):
                l = max(l, len(s))
            else: 
                break

    return l


