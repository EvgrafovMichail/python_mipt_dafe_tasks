def count_unique_words(text: str) -> int:
    answ = []
    buffer = ""
    for i in text:
        if i.islower() or i.isupper():
            buffer += i.lower()
        elif i in "0123456789":
            buffer += i
        elif i == " " and buffer != "" and buffer not in answ:
            answ.append(buffer)
            buffer = ""
        elif i == " ":
            buffer = ""
    if buffer != "" and buffer not in answ:
        answ.append(buffer)
    return len(answ)
