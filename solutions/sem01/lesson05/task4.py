def unzip(compress_text: str) -> str:
    text = ""
    compress_text += " "
    pul = ""
    k=0
    for i in compress_text:
        if i ==" " or i in "0123456789":
            text += pul
            pul = ""
            k += 1
            continue
        if i == "*":
            ind = 1
            number = 0
            while compress_text[k+ind].isdigit() and k + ind <len(compress_text):
                number *= 10
                number += int(compress_text[k+ind])
                ind+=1

            text += pul*int(number)
            pul = ""
            k += 1
            continue
        k += 1
        pul += i
        
    
    text += pul

    return text