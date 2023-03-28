"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

my_list_letter = ['разработка', 'сокет', 'декоратор']
for line in my_list_letter:
    print('Тип переменной: {}\n'.format(type(line)))
    print('Содержание переменной: {}\n'.format(line))

my_list_unicode = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
for line in my_list_unicode:
    print('Тип переменной: {}\n'.format(type(line)))
    print('Содержание переменной: {}\n'.format(line))

    
#2 способ
unicode_list = []
for line in my_list_letter:
    uni_el = line.encode('unicode_escape')
    unicode_list.append(uni_el)
print(unicode_list)
for line in unicode_list:
    dec_el = line.decode('unicode_escape')
    print('Тип переменной: {}\n'.format(type(line)))
    print(f'Содержание переменной: {dec_el}\n')
