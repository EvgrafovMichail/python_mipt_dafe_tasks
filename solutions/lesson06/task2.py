def get_len_of_longest_substring(text: str) -> int:
    if not text:
        return 0

    sym = {}
    maxx = 0
    left = 0

    for right in range(len(text)):
        if text[right] in sym and sym[text[right]] >= left:
            maxx = max(maxx, right - left)
            left = sym[text[right]] + 1

        sym[text[right]] = right

    maxx = max(maxx, len(text) - left)
    return maxx
