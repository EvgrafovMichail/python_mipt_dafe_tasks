def is_palindrome(text: str) -> bool:
    text = text.lower()
    return text == text[::-1]