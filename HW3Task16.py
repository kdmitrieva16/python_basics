# A[1..N]. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X


import random

a = []
n = int(input("Введите требуемую длину массива  N: "))
for i in range(n):
    a.append(random.randint(0, 10))
print(a)
x = int(input("Введите число X: "))
print(a.count(x))