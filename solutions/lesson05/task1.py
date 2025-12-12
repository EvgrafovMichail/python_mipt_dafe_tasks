def is_palindrome(text: str) -> bool:
    # ваш код
    if len(text) == 0:
        return True
    text = text.lower()
    mirrored_text = ""
    for i in range(len(text)):
        mirrored_text += text[-1 - i]
    if mirrored_text == text:
        return True
    return False
