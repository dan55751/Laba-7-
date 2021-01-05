#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и определяет, сколько в нем слов,
# состоящих из не менее чем семи букв.

if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()

    text.replace(".", " ")
    text.replace(",", " ")
    text.replace(";", " ")
    text.replace("!", " ")
    text.replace("?", " ")
    sentences = text.split(" ")

    for i in text:
        text.replace(i, ' ')
    sentences = [i for i in sentences if len(i) > 6]
    print(f'{sentences}')
    print(f'Слов, состоящих из 7 букв: {len(sentences)}')
