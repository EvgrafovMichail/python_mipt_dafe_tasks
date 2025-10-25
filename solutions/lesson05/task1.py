def is_palindrome(text: str) -> bool:
    i = len(text) - 1
    j = 0

    while i > j:
        if abs(ord(text[i]) - ord(text[j])) == 32:
            i -= 1
            j += 1
            continue
        if text[i] != text[j]:
            return False
        i -= 1
        j += 1

    return True
