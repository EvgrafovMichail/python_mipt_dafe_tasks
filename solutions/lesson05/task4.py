def unzip(compress_text: str) -> str:
    splitted_compress_text = [i for i in compress_text.split()]

    unziped_str = ""
    for ziped_substr in splitted_compress_text:
        repeat_cnt = ""
        substr = ""

        for symb in range(len(ziped_substr)):
            if ziped_substr[symb].isalpha():
                substr += ziped_substr[symb]
            elif ziped_substr[symb].isdigit():
                repeat_cnt += ziped_substr[symb]

        if repeat_cnt == "":
            unziped_str += substr
        else:
            unziped_str += substr * int(repeat_cnt)

    return unziped_str
