def get_len_of_longest_substring(text: str) -> int:
    symb = {}
    maxlen = 0
    left = 0
    for right in range(len(text)):
        while text[right] in symb:
            symb.pop(text[left])
            left += 1
        if right - left + 1 > maxlen:
            maxlen = right - left + 1
        symb[text[right]] = right
    return maxlen
