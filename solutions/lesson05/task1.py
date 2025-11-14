def is_palindrome(text: str) -> bool:
    text = text.lower()
    if text[::-1] == text:
        return True
    else:
        return False
