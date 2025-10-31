def is_palindrome(text: str) -> bool:
    text = text.lower()

    return text[::-1] == text
