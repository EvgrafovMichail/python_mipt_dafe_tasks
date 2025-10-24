def is_palindrome(text: str) -> bool:
    for i in range(len(text) // 2):
        if text[i].lower() != text[-i - 1].lower():
            return False

    return True
