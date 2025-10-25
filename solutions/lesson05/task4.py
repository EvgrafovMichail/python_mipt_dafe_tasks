def unzip(compress_text: str) -> str:
    if not compress_text:
        return ''
    
    lst = []
    tokens = compress_text.split()
    
    for token in tokens:
        if "*" in token:
            string, num = token.split('*')
            lst.append(string * int(num))
        else:
            lst.append(token)
    return "".join(lst)

#print(unzip(input()))
