n = int(input("Введите 6-ти значный номер билета: "))
d6 = n % 10  # Определяем 6 цифру в числе
n = n // 10  # убираем 6 цифру из исходного числа
d5 = n % 10  # Определяем 5 цифру в числе
n = n // 10  # Убираем 5 цифру
d4 = n % 10  # Определяем 4 цифру в числе
n = n // 10  # Убираем 4 цифру
d3 = n % 10  # Определяем 3 цифру в числе
n = n // 10  # Убираем 3 цифру
d2 = n % 10  # Определяем 2 цифру в числе
n = n // 10  # Убираем 2 цифру
if n + d2 + d3 == d4 + d5 + d6:
    print("Билет счастливый")
else:
    print("Нет")