# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# num = list(map(int, input("Введите числа для создания списка: ")))

def multiplication_lst(lst):
    l = len(lst) // 2

    for i in range(l):
        new_lst = [lst[i] * lst[len(lst) - i - 1]]
        print(new_lst)

lst = list(map(int, input("Введите числа через пробел: ").split()))
multiplication_lst(lst)