n = int(input("Введите любое целое положительное трехзначное число: "))
d1 = n % 10  # Определяем третью цифру в числе
n = n // 10  # убираем третью цифру из исходного числа
d2 = n % 10  # Определяем вторую цифру в числе
n = n // 10  # Убираем вторую цифру, остается 1 цифра исходного числа
result = n + d1 + d2  # Складываем  1, 2 и 3 цифры
print(f"Сумма цифр числа: {n}+{d1}+{d2}={result}")