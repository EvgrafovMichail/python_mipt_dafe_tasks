def is_palindrome(text: str) -> bool:
    text = text.lower()
    reversed_text = text[::-1]
    return text == reversed_text
