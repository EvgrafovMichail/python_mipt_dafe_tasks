def get_len_of_longest_substring(text: str) -> int:
    k = 0
    mk = 0
    s = ""
    for i in text:
        if i not in s:
            k += 1
            s += i
            mk = max(k, mk)
        else:
            s = s[s.index(i) + 1 :] + i
            k = len(s)
    return mk
