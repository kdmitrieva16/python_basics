import random

a = []
n = int(input("Введите количество монет N: "))
for i in range(n):  # Генерируется положение монет 1-орел, 0-решка
    a.append(random.randint(0, 1))
print(a)
count_a = 0
count_b = 0
for el in a: #Рассчитываем количество монет в положении орел и решка
    if el == 0:
        count_a += 1
    else:
        count_b += 1
if count_a < count_b:
    print(f'Надо перевернуть {count_a} монет')
else:
    print(f'Надо перевернуть {count_b} монет')