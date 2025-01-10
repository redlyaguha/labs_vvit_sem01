def write_text(text):
    with open('user_input.txt', 'w') as file:
        file.write(text)
        while True:
            print('Перейти на строчку ниже? \n 1 - Да \n 2 - Выйти')
            temp = input()
            if temp == '1':
                file.write('\n')
                print('Напишите текст, который хотите добавить:')
                add_temp = input()
                file.write(add_temp)
            if temp == '2':
                break
            else:
                print('Вы ввели некорректные данные')


def add_text(text):
    with open('user_input.txt', 'a') as file:
        try:
            file.read()
        except:
            print('Файл пока пуст')
            return 0

        file.write(text)
        while True:
            print('Перейти на строчку ниже? \n 1 - Да \n 2 - Выйти')
            temp = input()
            if temp == '1':
                file.write('\n')
                print('Напишите текст, который хотите добавить:')
                add_temp = input()
                file.write(add_temp)
            if temp == '2':
                break
            else:
                print('Вы ввели некорректные данные')


def delete_text(text):
    open('file.txt', 'w').close()


def check_text():
    with open('user_input.txt', 'r') as file:
        content = file.read()
    return content


while True:
    print(
        'Выберите действие: \n 1 - Перезаписать файл \n 2 - Добавить текст к существующей записи \n 3 - Удалить записи \n 4 - Прочесть содержимое файла \n 5 - Выход')
    i = input()
    if i == '1':
        print('Напишите текст, которым хотите перезаписать файл:')
        add = input()
        write_text(add)
    if i == '2':
        print('Напишите текст, который хотите добавить:')
        add = input()
        add_text(add)
    if i == '3':
        add = ''
        print('Файл очищен')

        delete_text(add)
    if i == '4':
        print(check_text())
    if i == '5':
        exit()
    else:
        print('Введены некорректные данные')
