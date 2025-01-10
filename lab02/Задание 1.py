def great(name):
    print('Hello,', name)


def square(number):
    try:
        float(number)
        return float(number) ** 2
    except ValueError:
        print('Вы ввели не число!')
        exit()


def max_of_two(x, y):
    try:
        float(x)
        float(y)
    except ValueError:
        print('Вы ввели не число!')
        exit()

    if float(x) < 0 and float(y) < 0:
        return y if x > y else x
    else:
        return max(x, y)


choice = input('Выбирите функцию: 1.greet 2.square 3.max_of_two (число):')

if choice == '1':
    Name = input('Введите имя пользователя: ')
    great(Name)

elif choice == '2':
    Number = input('Введите число: ')
    print(square(Number))

elif choice == '3':
    X = input('Первое число: ')
    Y = input('Второе число: ')
    print(max_of_two(X, Y))

else:
    print('Функция не найдена')
