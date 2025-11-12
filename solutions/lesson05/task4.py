def unzip(compress_text: str) -> str:
    if "*" in compress_text:
        arr_text = compress_text.split()
        compress_text = str()
        for i in range(0, len(arr_text)):
            i_str = arr_text[i].split("*")
            if len(i_str) == 1:
                compress_text += i_str[0]
            else:
                for j in range(0, int(i_str[1])):
                    compress_text += i_str[0]
    else:
        return compress_text.replace(" ", "")
    return compress_text
