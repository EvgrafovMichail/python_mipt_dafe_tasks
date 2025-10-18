def is_palindrome(text: str) -> bool:
    # ваш код
    text = text.lower()
    if text == text[::-1]:
        return True
    return False
