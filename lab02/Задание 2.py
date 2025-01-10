def describe_person(name, age=30):
    try:
        float(age)
        return name, age
    except ValueError:
        print('Вы ввели не число!')
        exit()


def is_prime(number):
    number = input('Введите число на проверку: ')
    try:
        float(number)
        if float(number) % 2 == 0:
            return True
        else:
            return False
    except ValueError:
        print('Вы ввели не число!')
        exit()


choice = input('Выбирите функцию: 1.describe_person 2.is_prime(число):')
if choice == '1':
    Name = input('Введите ваше имя: ')
    Age = input('Введите возраст: ')
    print(describe_person(Name, Age))
elif choice == '2':
    print(is_prime(''))
else:
    print('Функция не найдена')
