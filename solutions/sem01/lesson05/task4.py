def unzip(compress_text: str) -> str:
    zip = compress_text.split()
    uncompressed_text = ""
    for substring_and_count in zip:
        substring = ""
        count = 0
        for symbol in substring_and_count:
            if symbol.isalpha():
                substring += symbol
            else:
                break
        multiplier = 1
        for digit in substring_and_count[::-1]:
            if digit.isdigit():
                count += multiplier * int(digit)
                multiplier *= 10
            else:
                break
        if multiplier == 1:
            count = 1
        uncompressed_text += substring * count

    return uncompressed_text
