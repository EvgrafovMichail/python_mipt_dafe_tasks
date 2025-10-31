def is_palindrome(text: str) -> bool:
    del_text = list(text.lower())
    out = []
    for i in del_text:
        out.insert(0, i)
    if list(text.lower()) == out:
        answer = True
    else:
        answer = False
    return answer
