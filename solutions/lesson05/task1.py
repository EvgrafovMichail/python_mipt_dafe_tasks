def is_palindrome(text: str) -> bool:
    text = text.lower()
    text_reverse = text[::-1]
    if text == text_reverse:
        return True
    return False
