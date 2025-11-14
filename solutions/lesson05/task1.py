def is_palindrome(text: str) -> bool:
    return True if (text := text.lower()) == text[::-1] else False
