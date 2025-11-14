def get_len_of_longest_substring(text: str) -> int:
    ans = 0
    for left in range(len(text)):
        strM = set()
        for r in range(left, len(text)):
            if text[r] not in strM:
                strM.add(text[r])
            else:
                ans = max(ans, len(strM))
                break
        else:
            ans = max(ans, len(strM))
    return ans
