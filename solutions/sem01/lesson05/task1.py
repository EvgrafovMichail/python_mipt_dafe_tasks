def is_palindrome(text: str) -> bool:
    n = len(text)
    text = text.lower()
    for i in range(n):
        if text[i] != text[n - i - 1]:
            return False
    return True
