#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randint

number = int(input('Введите размер списка '))
mass = []
mass2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(mass)):
    while i < len(mass)/2 and number > len(mass)/2:
        number = number - 1
        a = mass[i] * mass[number]
        mass2.append(a)
        i += 1

print(mass)
print(mass2)