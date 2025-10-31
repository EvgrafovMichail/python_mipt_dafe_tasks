def get_len_of_longest_substring(text: str) -> int:
    start = 0
    maxlen = 0
    while start < len(text):
        substr = ""
        for i in range(start, len(text)):
            if text[i] not in substr:
                substr += text[i]
            else:
                break
        maxlen = max(maxlen, len(substr))
        start += 1
    return maxlen
