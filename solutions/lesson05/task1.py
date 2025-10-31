def is_palindrome(text: str) -> bool:
    if len(text) == 0:
        return True

    k = 0
    text = text.upper()

    for i in range(len(text) // 2 + 1):
        if text[i] == text[len(text) - 1 - i]:
            k += 1

    if k == len(text) // 2 + 1:
        return True

    return False
