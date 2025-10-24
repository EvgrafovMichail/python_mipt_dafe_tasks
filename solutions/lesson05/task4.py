def unzip(compress_text: str) -> str:
    result = ''

    arh_elements = compress_text.split()
    
    for element in arh_elements:
        if '*' in element:
            lst = element.split('*')
            result += lst[0] * int(lst[1])
        else:
            result += element

    return result