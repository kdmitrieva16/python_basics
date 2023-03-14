# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
# максимума)
import random

a = []
n = int(input("Введите требуемую длину массива  N: "))
for i in range(n):
    a.append(random.randint(0, 100))
print(a)
min_el = int(input('Enter the number min : '))
max_el = int(input('Enter the number max : '))
for i, j in enumerate(a):
    if j > min_el and j < max_el:
        print(i)
