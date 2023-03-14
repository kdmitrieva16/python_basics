# Реализовать структуру «Рейтинг», представляющую собой не
# возрастающий набор натуральных чисел
# (каждый элемент ряда меньше или равен предыдущему).
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {my_list}')
n = int(input("Введите натуральное число n: "))
my_list.append(n)
my_list.sort(reverse=True)
print(f'Рейтинг - {my_list}')
