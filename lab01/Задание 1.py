def is_number_tryexcept(a):
    try:
        float(a)
    except ValueError:
        print('Вы ввели не число!')
        exit()


s = input('Введите число: ')

i = 1
is_number_tryexcept(s)
s = int(s)
if i > s:
    while s - 1 != i:
        print(i)
        i -= 1
else:
    while s + 1 != i:
        print(i)
        i += 1
