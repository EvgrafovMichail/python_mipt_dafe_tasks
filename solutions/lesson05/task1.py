def is_palindrome(text: str) -> bool:
    lower_text = text.lower()
    if lower_text == lower_text[::-1]:
        return True
    else:
        return False