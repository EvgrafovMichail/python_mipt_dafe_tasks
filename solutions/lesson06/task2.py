def get_len_of_longest_substring(text: str) -> int:
    l = 0
    mx = 0
    for r in range(len(text)):
        symbol = text[r]
        while symbol in text[l:r]:
            l += 1
        if r - l + 1 > mx:
            mx = r - l + 1
    return mx
