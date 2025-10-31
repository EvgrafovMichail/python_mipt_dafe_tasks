def get_len_of_longest_substring(text: str) -> int:
    if not text:
        return 0

    left = 0
    unique_ch = set()
    longest = 0

    for right in range(len(text)):
        #        unique_ch.add(text[right])
        while text[right] in unique_ch:
            unique_ch.remove(text[left])
            left += 1

        unique_ch.add(text[right])

        if right - left + 1 >= longest:
            longest = right - left + 1

    return longest


# print(get_len_of_longest_substring(input()))
# abcabcpw
