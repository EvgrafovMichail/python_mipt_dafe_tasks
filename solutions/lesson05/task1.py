def is_palindrome(text: str) -> bool:
    # ваш код
    inverted_text = text.upper()
    if inverted_text[::-1] == inverted_text:
        return True
    return False