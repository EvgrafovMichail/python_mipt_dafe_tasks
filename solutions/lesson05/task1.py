def is_palindrome(text: str) -> bool:
    for i in range(len(text) // 2):
        if text[i].lower() != text[len(text) - 1 - i].lower():
            return False
    return True
