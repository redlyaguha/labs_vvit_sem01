def open_file(i):
    if i == 1:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    if i == 0:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())


def file_true():
    try:
        file = open(file_name, 'r')
    except FileNotFoundError as error:
        print('Файл не найден:', error)
        exit()


print('Введите название файла:')
file_name = input()
file_true()
print('Каким способ хотите прочесть файл?')
print('1 - целиком/2 - построчно')
c = input()
if c == '1':
    print(open_file(1))
elif c == '2':
    open_file(0)
else:
    print('Вы ввели некорректные данные')
