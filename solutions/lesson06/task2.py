def length_of_longest_substring(text):
    symbols = set()
    left = 0
    ans = 0

    for right in range(len(text)):
        if text[right] not in symbols:
            symbols.add(text[right])
            ans = max(ans, len(symbols))
        else:
            while text[right] in symbols:
                symbols.remove(text[left])
                left += 1
            symbols.add(text[right])

    return ans
