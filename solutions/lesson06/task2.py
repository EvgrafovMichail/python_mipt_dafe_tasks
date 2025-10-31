def get_len_of_longest_substring(text: str) -> int:
    # проверяем символы толкая вперед right 
    # если символ повторился то притягиваем left на место повтора
    left = 0
    max = 0 # длинна самой длинной последовательности 
    unique_symbols = {} # словарь с каждой буквой и ее порядковым номером 


    for right in range(len(text)):
        symbols = text[right]

        # перетяжка left
        if symbols in unique_symbols:
            left = unique_symbols[symbols] + 1

        # если все гуд то увеличиваем расстояние между right и left 
        # также имеем ввиду max чтобы запоминать самую длинну последовательнось
        else:
            if max <= (right - left):
                max += 1
        
        # запоминаем или обновляем порядковый номер буквы
        unique_symbols[symbols] = right

        

    return max