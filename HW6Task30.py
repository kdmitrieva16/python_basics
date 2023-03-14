a1 = int(input("Введите первый элемент последовательности а1: "))
d = int(input("Введите разность d: "))
n = int(input("Введите количество элементов последовательности n: "))
my_list = [a1]
# my_list[0] = a
for i in range(2, n):
    a = a1 + (i - 1) * d
    my_list.append(a)
print(my_list)

# 2 способ
A = [a1 + (i - 1) * d for i in range(1, n)]
print(*A)
