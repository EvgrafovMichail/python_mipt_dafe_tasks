def is_palindrome(text: str) -> bool:
    return text[-1::-1].lower() == text.lower()
