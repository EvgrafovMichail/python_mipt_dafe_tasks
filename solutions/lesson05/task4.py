def unzip(compress_text: str) -> str:
    compress_text = compress_text + ' '
    text = []
    i0 = 0
    for i in range(len(compress_text)):
        if compress_text[i] == ' ':
            text.append(compress_text[i0:i])
            i0 = i + 1
    compress_text = ''
    for i in range (len(text)):
        if "*" in text[i]:
            i0 = text[i].find('*')
            compress_text += text[i][:i0] * int(text[i][i0+1:])
        else:
            compress_text += text[i]

    return compress_text
