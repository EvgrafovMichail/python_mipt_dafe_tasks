def is_palindrome(text: str) -> bool:
    text_lower = text.lower()
    return text_lower == text_lower[::-1]
