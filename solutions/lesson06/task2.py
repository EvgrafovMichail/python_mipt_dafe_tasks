def get_len_of_longest_substring(text: str) -> int:
    dict = {}
    otv = 0
    mins = 0
    for i in range(len(text)):
        c = text[i]
        if c not in dict:
            dict[c] = i
        else:
            mins = max(mins, dict[c] + 1)
            dict[c] = i
        otv = max(otv, i - mins + 1)
    return otv


print(get_len_of_longest_substring("abcd"))
