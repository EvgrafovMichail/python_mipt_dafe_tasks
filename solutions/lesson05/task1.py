def is_palindrome(text: str) -> bool:
    text = text.upper()
    if text == text[::-1]:
        return True
    return False
