n = int(input("Введите целое положительное число: "))
temp = str(n)
nn = temp + temp
nnn = temp + temp + temp
result = n + int(nn) + int(nnn)
print(f"Результат равен: {result}")