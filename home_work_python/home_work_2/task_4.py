# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

# from random import Random, randint

'''
n = int(input('Введите число: '))
numbers = []
numbers_for_multiplication = []
for i in range(-n, n+1):
    numbers.append(i)
numbers_for_multiplication = numbers

print(numbers_for_multiplication)

multiplication_numbers = []
# print('Введите позиции списка для нахождения произведения, через запятую: ')
# multiplication_numbers.append(int(input()))
# print(multiplication_numbers)
len_multiplication_numbers = len(numbers_for_multiplication)
print(len_multiplication_numbers)
count = 1
if count < 5:
    multiplication_numbers.append(int(input()))
    count = count + 1
    print(multiplication_numbers)
    
else: 
    print('хватит')
'''

n = int(input('Введите число: '))
numbers = []
numbers_for_multiplication = []
for i in range(-n, n+1):
    numbers.append(i)
numbers_for_multiplication = numbers

print(numbers_for_multiplication)
print(f'Длинна списка  от числа {n} равно {len(numbers_for_multiplication)}')

x = int(input('Введите первый индекс для умнржения: '))
y = int(input('Введите второй индекс для умножения: '))
# z = 0
if x < len(numbers_for_multiplication) - 1 and y < len(numbers_for_multiplication) - 1:
    z = numbers_for_multiplication[x] * numbers_for_multiplication[y]
    print(z)
else:
    print('Числа вне пределов длинны списка')

