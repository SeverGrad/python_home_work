# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fabionchi(n):
    if n in [1, 2]:
        return 1
    else:
        return fabionchi(n - 1) + fabionchi(n - 2)



def negafabionchi(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


lst = [0]
user_number = int(input('Введи число: '))
for e in range(1, user_number +1):
    lst.append(fabionchi(e))
    lst.insert(0, negafabionchi(e))

print(lst)