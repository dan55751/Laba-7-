#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение

if __name__ == '__main__':
    persons = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Введите фамилию и имя ")
            tel_number = input("Введите номер телефона ")
            birthday = input("Введите дату рождения, типа 02.01.2020 ")

            person = {
                'name': name,
                'tel_number': tel_number,
                'birthday': birthday,
            }

            persons.append(person)
            if len(person) > 1:
                persons.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 16
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^16} |'.format(
                    "№",
                    "Фамилия и имя",
                    "Номер телефона",
                    "Дата рождения"
                )
            )
            print(line)

            for idx, person in enumerate(persons, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>16} |'.format(
                        idx,
                        person.get('name', ''),
                        person.get('tel_number', ''),
                        person.get('birthday', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):
            parts = command.split(maxsplit=1)
            count = 0
            for person in persons:
                birthday_month = person.get('birthday', '').split('.')
                if parts[1] == birthday_month[1]:
                    count += 1
                    print(
                        '{:>4}: {} {}'.format(count, person.get('name', ' '), person.get('tel_number', ' '))
                    )
            if count == 0:
                print("В этом месяце ни у кого нет дня рождения")

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'r') as f:
                persons = json.load(f)

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'w') as f:
                json.dump(persons, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить товары;")
            print("list - вывести список товаров;")
            print("select <месяц> - запросить иениников в выбранном месяце")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
