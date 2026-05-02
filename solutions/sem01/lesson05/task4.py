def unzip(compress_text: str) -> str:
    compress_text_split = compress_text.split()
    lst = []
    for sub_str in compress_text_split:
        if "*" in sub_str:
            zvezd_index = sub_str.find("*")
            lst.append(sub_str[:zvezd_index:] * int(sub_str[zvezd_index + 1 : :]))
        else:
            lst.append(sub_str)
    compress_text = "".join(lst)
    return compress_text
