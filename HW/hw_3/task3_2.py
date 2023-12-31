# В большой текстовой строке подсчитать количество встречаемых слов и вернуть
# 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# Пример:
# Ввод:
# текст отсюда(https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D0%BB%D0%B8,_%D0%A1%D0%B8%D0%BB%D1%8C%D0%B2%D0%B0%D0%BD%D1%83%D1%81)
#
# Вывод:
#
# Слово "в", 22 раз
# Слово "и", 11 раз
# Слово "году", 9 раз
# Слово "с", 4 раз
# Слово "морли", 4 раз
# Слово "по", 3 раз
# Слово "степень", 3 раз
# Слово "института", 3 раз
# Слово "был", 3 раз
# Слово "памятников", 3 раз

def popular_words(text: str):
    my_dict = {}
    text_list = text.lower().split()
    text_list_new = [''.join(filter(str.isalpha, a)) for a in text_list]

    while '' in text_list_new:
        text_list_new.remove('')

    for word in text_list_new:
        my_dict.setdefault(word, text_list_new.count(word))

    num_words = 1
    while num_words <= 10:
        num_words += 1
        max_key = max(my_dict,  key=my_dict.get)
        print(f'{max_key:>5}  =  {my_dict[max_key]}')
        my_dict.pop(max_key)

    return my_dict




text = "Джонатан Джостар — Главный герой первой части манги. Родом из благородной семьи Джостаров. " \
       "Мать Джонатана умерла практически сразу после его рождения, защищая его своим телом во время " \
       "крушения повозки. Джонатан рос сильным, но когда в поместье прибыл Дио, он всеми способами " \
       "пытался сломить волю Джонатана: оскорблениями, побоями и убийством его любимого пса по кличке " \
       "Дэнни. При этом отец Джонатана был всегда на стороне Дио, будучи уверенным, что Джонатан лжёт " \
       "об издевательствах и просто хочет «выжить» Дио из поместья. Прошло 7 лет, Дио и Джонатан к тому " \
       "времени стали более нормально уживаться. Впрочем вскоре Джонатан узнаёт о том, что Дио " \
       "собирается отравить его отца, чтобы побыстрее заполучить наследство. Этому не суждено сбыться, " \
       "планы Дио были разрушены, из-за чего последний случайно находит каменную маску, превратившую " \
       "его в вампира. В тяжёлом бою последний Джостар одолевает его, сжигая дотла поместье. " \
       "Джонатан начинает путешествовать в поисках Дио, чтобы уничтожить его. К нему присоединяется " \
       "барон Цеппели, обладающий необычной силой «Хамон», овладение которой поможет одолеть вампира. " \
       "Так Джонатан начинает обучаться использованию данной силы. Дио направляет своих подчинённых — " \
       "убить Джонатана, но герой одолевает их всех. В конце концов он фактически уничтожает Дио, " \
       "введя Хамон в его тело, но тот спасается, отделив свою голову. После помолвки Джонатан и Эрина " \
       "отправляются на круизный корабль в Америку. Но там оказывается и Брандо, который намерен " \
       "заполучить тело Джонатана, тогда он обратил всех людей на корабле в зомби. Джонатан подрывает " \
       "корабль, потопив себя, Дио и остальных. Эрина спасается вместе с подобранным младенцем. " \
       "Однако позже выясняется, что Дио всё же заполучил тело своего врага."

print(popular_words(text))

