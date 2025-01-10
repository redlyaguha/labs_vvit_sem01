def is_number_tryexcept(a, b):
    try:
        float(a)
        float(b)
        return a, b
    except ValueError:
        print('Вы ввели не число!')
        exit()


b = input('Введите первое число: ')
a = input('Введите второе число: ')
is_number_tryexcept(a, b)

if float(a) < 0 and float(b) < 0:
    print(b if a > b else a)
else:
    print('Большее число: ', max(a, b))
