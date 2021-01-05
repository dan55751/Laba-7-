#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('text.txt', 'r', encoding="utf8") as f:
        text = f.read()

    # Заменить символы конца предложения.
    text = text.replace("!", ".")
    text = text.replace("?", ".")

    # Удалить все многоточия.
    while ".." in text:
        text = text.replace("..", ".")

    # Разбить текст на предложения.
    sentences = text.split(".")

    # Вывод предложений с запятыми.
    for sentence in sentences:
        if "," in sentence:
            symb = list(sentence)
            symb.append('.')
            strin = ''
            strin = strin.join(symb)
            print("{}".format(strin))
