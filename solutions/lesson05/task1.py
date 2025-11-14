def is_palindrome(text: str) -> bool:
    return text.lower() == text.lower()[::-1]