# примеры форматирования текста
print("Привет, " + "мир!")
print('меня зовут %(name)s, мне %(year)s' % {'name': 'Айнур', 'year': 34})
print('Я учусь в {title}{postfix} {title}' .format(title='Урбан', postfix='-university'))
print(f'{"Urban" * 2} это лучший университет!')