def get_len_of_longest_substring(text: str) -> int:
    begin, end = 0, 0
    longest = 0

    chars = set()

    while end < len(text):
        if text[end] in chars:
            while text[end] in chars:
                chars.remove(text[begin])
                begin += 1

            chars.add(text[end])

        else:
            chars.add(text[end])

        longest = max(longest, end - begin + 1)
        end += 1

    return longest


print(get_len_of_longest_substring("112233"))
