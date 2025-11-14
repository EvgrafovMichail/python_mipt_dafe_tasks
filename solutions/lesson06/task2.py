def get_len_of_longest_substring(text: str) -> int:
    maxlen = 0
    start = 0
    while len(set(text[start:])) != len(text[start:]):
        chars = {}
        for i in range(start, len(text)):
            if text[i] not in chars:
                chars[text[i]] = i
            else:
                maxlen = max(len(chars), maxlen)
                start = chars[text[i]] + 1
                break
    else:
        maxlen = max(maxlen, len(text[start:]))
    return maxlen


print(get_len_of_longest_substring("aab"))
