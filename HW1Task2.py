time_from_user = int(input("Введите время в секундах: "))
hour = time_from_user / 3600
minute = time_from_user / 60

print(f'Время в формате ч:м:с -  {hour}:{minute}:{time_from_user}')