def is_palindrome(text: str) -> bool:
    text = text.lower()
    n = len(text)
    for i in range(n - 1):
        if text[i] != text[-(i + 1)]:
            return False
    else:
        return True


print(is_palindrome("Aa"))
