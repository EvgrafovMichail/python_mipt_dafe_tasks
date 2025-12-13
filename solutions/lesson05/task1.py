def is_palindrome(text: str) -> bool:
    t = len(text)
    text = text.lower()
    for i in range(t // 2):
        if text[i] != text[-i - 1]:  # ну это получше чем с таким срезом text[::-1] сравнивать
            return False
    return True
