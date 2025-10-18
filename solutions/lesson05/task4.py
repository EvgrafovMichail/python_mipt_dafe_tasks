def unzip(compress_text: str) -> str:
    numbers = '0123456789'
    litters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    unfolded_text = ''
    word = ''
    multiplier = ''
    for i in range(len(compress_text)):
        char = compress_text[i]
        if char in litters:
            word += char
        if char in numbers:
            multiplier += char
        if char == ' ' or i == len(compress_text) - 1:
            print(word, multiplier)
            if multiplier:
                unfolded_text += word*(int(multiplier)-1)
            unfolded_text += word
            word = ''
            multiplier = ''
    return unfolded_text
