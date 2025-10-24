def unzip(compress_text: str) -> str:
    elements = compress_text.split(" ")
    string = ""

    for i in elements:
        if "*" in i:
            el_i = i.split("*")
            string += el_i[0] * int(el_i[1])

        else:
            string += i

    return string
