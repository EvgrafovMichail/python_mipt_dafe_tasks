def get_len_of_longest_substring(text: str) -> int:
    d, cur, rec = dict(), str(), int()
    for i in text:
        ind = d.get(i, -1)
        if ind == -1:
            cur += i
            d[i] = len(cur)
            rec = max(rec, len(cur))
        else:
            cur = cur[ind:]
            del d[i]
            d = {i: d[i] - ind for i in d.keys()}
            cur += i
            d[i] = len(cur)
    rec = max(rec, len(cur))
    return rec


if __name__ == "__main__":
    print(get_len_of_longest_substring("abcabcbbxyz"))
