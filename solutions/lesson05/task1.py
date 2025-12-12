def is_palindrome(text: str) -> bool:
    text = text.upper()
    s = text[::-1]
    if s == text:
        return True
    return False
