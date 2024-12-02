def custom_write(file_name: str, strings: list[str, ...]) -> dict[tuple[int, int], str]: # возвращает словарь, где ключом является кортеж из двух целых чисел, и следующий ключ это строка.
    file = open(file_name, 'w')
    res = {}
    for i in range(len(strings)):
        pos = file.tell()
        res[(i + 1, pos)] = strings[i]
        file.write(f'{strings[i]}\n')
    file.close()
    return res

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

