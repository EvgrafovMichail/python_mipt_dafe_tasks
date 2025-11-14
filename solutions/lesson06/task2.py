def get_len_of_longest_substring(text: str) -> int:
    if text == "":
        return 0
    ans = 1
    sub = text[0]
    for i in range(len(text) - 1):
        if text[i + 1] not in sub:
            sub += text[i + 1]
            ans = max(ans, len(sub))
            continue
        sub = sub[sub.find(text[i + 1]) + 1 :] + text[i + 1]
    return ans
