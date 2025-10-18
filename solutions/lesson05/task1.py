def is_palindrome(text: str) -> bool:
    text = text.lower()
    if text == text[::-1]:
        return True
    return False
