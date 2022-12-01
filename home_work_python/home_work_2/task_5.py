# Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

from random import randint

def mix(lst):
    for i in range(0, len(lst)):
        new_i  = randint(0, len(lst) - 1)
        lst[i], lst[new_i] = lst[new_i], lst[i]

lst_ = [1, 2, 4, 6, 5, 8]
mix(lst_)
print(lst_)