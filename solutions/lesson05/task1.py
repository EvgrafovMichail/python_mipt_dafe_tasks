def is_palindrome(text: str) -> bool:
    if text == "":
        return True
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[-i - 1]:
            return False
    return True
