# # Напишите программу, которая принимает на вход вещественное 
# # число и показывает сумму его цифр.

# # *Пример:*

# # - 6782 -> 23
# # - 0.56 -> 11


num = input('Введите число: ')


def sum(num):
    if float(num) < 0:
        num = float(num) * (-1)
    number = 0

    for i in str(num):
        if i != str("."):
            number += int(i)
    return number


print(f'Сумма чисел равно: {sum(num)}')