def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        return f' {a}, {b}'  # Возвращаем сообщение об ошибке
    else:
        return f'{result: .3f}'  # Возвращаем результат сложения

# Вызываем функцию и выводим результат
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))