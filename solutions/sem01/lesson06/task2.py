def get_len_of_longest_substring(text: str) -> int:
    last_in = {}
    last_ok = 0
    ans = 0
    for i in range(len(text)):
        if text[i] not in last_in:
            last_in[text[i]] = i + 1
        else:
            last_ok = max(last_ok, last_in[text[i]])
            last_in[text[i]] = i + 1
        ans = max(ans, i - last_ok + 1)
    return ans
