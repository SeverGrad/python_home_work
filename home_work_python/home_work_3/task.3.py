# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



lst = list(map(float, input('Введите вещественные числа для создания списка: ').split()))
lst_2 = []
print(lst)
for i in lst:
    if i < len(lst):
        new_lst = [round(i % 1, 3)]
        i += 1
        print(new_lst)
        lst_2.extend(new_lst)
print(len(lst))
print(lst_2)

print(max(lst_2), min(lst_2))

dif = max(lst_2) - min(lst_2)     #Лист со значениями после запятой

print(round(dif, 2))
print(f'{lst} => {round(dif, 2)}')
