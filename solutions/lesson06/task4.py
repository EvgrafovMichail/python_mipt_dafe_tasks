def count_unique_words(text: str) -> int:
    # список нормальных символов
    char = "abcdefghijklmnopqrstuvwxyz0123456789"


    # создаем список слов и делаем буквы маленькими
    text = text.lower()
    list_text = text.split()

    sum_words = set()
    for word in list_text: 
        condition = False


        # удаляем сзади и спереди знаки препинания
        while word and not word[0] in char:
            word = word[1:]
        
        while word and not word[-1] in char:
            word = word[:-1]

        # жоска проверяем если там вообще символы и нормальные ли они 
        if word:
            for symbols in word:
                if symbols in char:
                   condition = True
        else:
            condition = False
        
        # создаем список set() (чтобы убрать повторки) со словами, которые подходят нам
        if condition == True:
            sum_words.add(word)

            
    # ну и в конце уверенно считаем количество слов
    final = len(sum_words) 

    return final 