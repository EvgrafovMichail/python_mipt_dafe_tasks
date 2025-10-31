def get_len_of_longest_substring(text: str) -> int:
    start = 0
    end = 1
    mx = len(text) if len(text) == len(set(text)) else 0
    if text != "":
        text += text[-1]
    while end < len(text) + 2:
        x = text[start:end]
        if len(x) == len(set(x)):
            end += 1
        else:
            mx = max(mx, end - start - 1)
            start += 1
    return mx
