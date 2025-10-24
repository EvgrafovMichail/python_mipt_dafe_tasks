def unzip(compress_text: str) -> str:
    mass = compress_text.split( )
    summ = ''
    if len(compress_text)<=2:
        return compress_text
    for i in mass:
        if '*' in i:
            summ += i.split('*')[0] * int(i.split('*')[1])
        else:
            summ += i
    return summ