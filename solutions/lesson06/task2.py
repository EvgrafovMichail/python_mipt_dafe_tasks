def get_len_of_longest_substring(text: str) -> int:
    lenght = 0
    n = len(text)
    for i in range(len(text)):
        for j in range(i + 1, n + 1):
            s = text[i:j]
            if len(s) == len(set(s)):
                lenght = max(lenght, len(s))
            else:
                break

    return lenght
