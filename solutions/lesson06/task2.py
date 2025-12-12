def get_len_of_longest_substring(text: str) -> int:
    i = 0
    j = 0
    unique = set()
    max_len = 1
    N = len(text)

    if not text:
        return 0

    while j < N:
        if text[j] in unique:
            unique.remove(text[i])
            i += 1
        else:
            unique.add(text[j])
            if j - i + 1 > max_len:
                max_len = j - i + 1
            j += 1

    return max_len


print(get_len_of_longest_substring(""))
